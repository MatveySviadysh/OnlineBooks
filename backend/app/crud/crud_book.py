from typing import List, Optional
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from schemas.book import BookCreate, BookUpdate, BookResponse
from api.book.helper_book import book_helper
from datetime import datetime, timedelta
import aiofiles
import os 
import aiohttp


class CRUDBook:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.books

    async def get_file_content(self, file_url: str) -> str:
        """Получение содержимого файла по URL"""
        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as response:
                if response.status != 200:
                    raise HTTPException(status_code=404, detail="Файл не найден")
                content = await response.text()
        return content

        
    async def create(self, book: BookCreate) -> BookResponse:
        """Создание новой книги"""
        new_book = book.dict()
        new_book["created_at"] = datetime.utcnow()
        new_book["updated_at"] = datetime.utcnow()
        
        result = await self.collection.insert_one(new_book)
        new_book["_id"] = result.inserted_id
        return book_helper(new_book)

    async def get_by_id(self, book_id: str) -> Optional[BookResponse]:
        """Получение книги по ID"""
        try:
            if not ObjectId.is_valid(book_id):
                raise HTTPException(status_code=400, detail="Неверный формат ID книги")
            book = await self.collection.find_one({"_id": ObjectId(book_id)})
            if not book:
                raise HTTPException(status_code=404, detail="Книга не найдена")
            return book_helper(book)
        except InvalidId:
            raise HTTPException(status_code=400, detail="Неверный формат ID книги")

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[BookResponse]:
        """Получение списка книг с пагинацией"""
        books = await self.collection.find().skip(skip).limit(limit).to_list(limit)
        return [book_helper(book) for book in books]

    async def get_popular(self, skip: int = 0, limit: int = 100) -> List[BookResponse]:
        """Получение популярных книг с рейтингом выше 3 с пагинацией"""
        books = await self.collection.find(
            {"rating": {"$gte": 3.0}}
        ).sort("views", -1).skip(skip).limit(limit).to_list(limit)
        return [book_helper(book) for book in books]

    async def get_recent(self, skip: int = 0, limit: int = 100) -> List[BookResponse]:
        """Получение недавно опубликованных книг (не старше 1 года), отсортированных по рейтингу"""
        one_year_ago = datetime.utcnow() - timedelta(days=365)
        books = await self.collection.find(
            {"publication_date": {"$gte": one_year_ago}}
        ).sort([
            ("rating", -1),
            ("publication_date", -1)
        ]).skip(skip).limit(limit).to_list(limit)
        return [book_helper(book) for book in books]

    async def get_all_without_limit(self) -> List[BookResponse]:
        """Получение всех книг без ограничений, отсортированных по рейтингу"""
        books = await self.collection.find().sort("rating", -1).to_list(None)
        return [book_helper(book) for book in books]

    async def get_count(self) -> int:
        """Получение общего количества книг"""
        return await self.collection.count_documents({})

    async def update(self, book_id: str, book_data: BookUpdate) -> BookResponse:
        """Обновление существующей книги"""
        try:
            if not ObjectId.is_valid(book_id):
                raise HTTPException(status_code=400, detail="Неверный формат ID книги")
                
            existing_book = await self.collection.find_one({"_id": ObjectId(book_id)})
            if not existing_book:
                raise HTTPException(status_code=404, detail="Книга не найдена")
            
            update_data = book_data.dict(exclude_unset=True)
            update_data["updated_at"] = datetime.utcnow()
            
            await self.collection.update_one(
                {"_id": ObjectId(book_id)}, 
                {"$set": update_data}
            )
            updated_book = await self.collection.find_one({"_id": ObjectId(book_id)})
            return book_helper(updated_book)
        except InvalidId:
            raise HTTPException(status_code=400, detail="Неверный формат ID книги")

    async def delete(self, book_id: str) -> None:
        """Удаление книги"""
        try:
            if not ObjectId.is_valid(book_id):
                raise HTTPException(status_code=400, detail="Неверный формат ID книги")
                
            result = await self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail="Книга не найдена")
        except InvalidId:
            raise HTTPException(status_code=400, detail="Неверный формат ID книги")

    async def delete_all(self) -> None:
        """Удаление всех книг"""
        await self.collection.delete_many({})

    async def get_by_genre(self, genre: str, skip: int = 0, limit: int = 100) -> List[BookResponse]:
        """Получение книг по жанру, отсортированных по рейтингу"""
        books = await self.collection.find(
            {"genre": genre}
        ).sort("rating", -1).skip(skip).limit(limit).to_list(limit)
        return [book_helper(book) for book in books]

    async def update_rating(self, book_id: str, rating: float) -> BookResponse:
        """Обновление рейтинга книги"""
        book = await self.collection.find_one({"_id": ObjectId(book_id)})
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return await self.update(book_id, BookUpdate(rating=rating))

    async def search_books(self, query: str, skip: int = 0, limit: int = 100) -> List[BookResponse]:
        """Поиск книг по названию или автору"""
        regex_query = {"$regex": query, "$options": "i"}  # 'i' для нечувствительности к регистру
        books = await self.collection.find({
            "$or": [
                {"title": regex_query},
                {"author": regex_query}
            ]
        }).skip(skip).limit(limit).to_list(limit)
        return [book_helper(book) for book in books]


def get_book_crud(db: AsyncIOMotorDatabase) -> CRUDBook:
    return CRUDBook(db)
