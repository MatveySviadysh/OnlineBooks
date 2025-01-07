from fastapi import APIRouter, Depends
from typing import List
from core.config import get_database
from schemas.book import BookCreate, BookUpdate, BookResponse
from crud.crud_book import get_book_crud

router = APIRouter(
    prefix="/books", 
    tags=["books"],
    responses={404: {"description": "Книга не найдена"}}
)

@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate, db = Depends(get_database)):
    """
    Создание новой книги со следующими полями:
    - title: название книги (макс. 200 символов)
    - author: автор книги (макс. 100 символов)
    - genre: жанр книги
    - publication_date: дата публикации
    - language: язык книги
    - page_count: количество страниц
    - rating: рейтинг книги (0-5)
    """
    crud_book = get_book_crud(db)
    return await crud_book.create(book)

@router.get("/", response_model=List[BookResponse])
async def get_all_books(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_all(skip, limit)

@router.get("/popular", response_model=List[BookResponse])
async def get_popular_books(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_popular(skip, limit)

@router.get("/all", response_model=List[BookResponse]) 
async def get_all_books_without_limit(db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_all_without_limit()

@router.get("/count", response_model=int)
async def get_books_count(db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_count()

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: str, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_by_id(book_id)

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: str, book_data: BookUpdate, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.update(book_id, book_data)

@router.delete("/delete-all", status_code=204)
async def delete_all_books(db = Depends(get_database)):
    """Удаление всех книг из базы данных"""
    crud_book = get_book_crud(db)
    await crud_book.delete_all()

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    await crud_book.delete(book_id)
