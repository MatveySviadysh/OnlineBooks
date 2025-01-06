from typing import List, Optional
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from schemas.book import BookCreate, BookUpdate, BookResponse
from api.book.helper_book import book_helper

class CRUDBook:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.books

    async def create(self, book: BookCreate) -> BookResponse:
        """Создание новой книги"""
        new_book = book.dict()
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

    async def get_all_without_limit(self) -> List[BookResponse]:
        """Получение всех книг без ограничений"""
        books = await self.collection.find().to_list(None)
        return [book_helper(book) for book in books]

    async def get_count(self) -> int:
        """Получение общего количества книг"""
        return await self.collection.count_documents({})

    async def update(self, book_id: str, book_data: BookUpdate) -> BookResponse:
        """Обновление существующей книги"""
        try:
            if not await self.collection.find_one({"_id": ObjectId(book_id)}):
                raise HTTPException(status_code=404, detail="Книга не найдена")
            update_data = book_data.dict(exclude_unset=True)
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
            if not await self.collection.find_one({"_id": ObjectId(book_id)}):
                raise HTTPException(status_code=404, detail="Книга не найдена")
            await self.collection.delete_one({"_id": ObjectId(book_id)})
        except InvalidId:
            raise HTTPException(status_code=400, detail="Неверный формат ID книги")

def get_book_crud(db: AsyncIOMotorDatabase) -> CRUDBook:
    return CRUDBook(db)
