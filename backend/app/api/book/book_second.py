from fastapi import APIRouter, Depends
from typing import List
from core.config import get_database
from schemas.book import BookCreate, BookUpdate, BookResponse
from crud.crud_book import get_book_crud
from api.book.helper_book import book_helper
import logging
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/book", 
    tags=["book"],
    responses={404: {"description": "Книга не найдена"}}
)

@router.get("/popular-with-audio", response_model=List[BookResponse])
async def get_popular_books_with_audio(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    print(f"Получение популярных книг с аудио, пропуск: {skip}, лимит: {limit}")
    
    # Corrected query to check for audio file path with a valid URL
    popular_books = await crud_book.collection.find(
        {
            "rating": {"$gte": 3.0},
            "audio_file_path": {
                "$exists": True,
                "$nin": ['', 'string'],  # Exclude empty strings and 'string'
                "$regex": "^https"  # Ensure it starts with 'https'
            }
        }
    ).sort("views", -1).skip(skip).limit(limit).to_list(limit)
    
    print(f"Найдено книг: {len(popular_books)}")
    
    # Log the IDs being returned
    for book in popular_books:
        logging.debug(f"Returning book ID: {book['_id']}")
    
    return [book_helper(book) for book in popular_books]

@router.get("/all-with-audio", response_model=List[BookResponse])
async def get_all_books_with_audio(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    print(f"Получение всех книг с аудио, пропуск: {skip}, лимит: {limit}")

    # Запрос для поиска всех книг с аудиофайлом
    books_with_audio = await crud_book.collection.find(
        {
            "audio_file_path": {
                "$exists": True,
                "$nin": ['', 'string'],  # Исключаем пустые строки и 'string'
                "$regex": "^https"  # Проверяем, что путь начинается с 'https'
            }
        }
    ).sort("views", -1).skip(skip).limit(limit).to_list(limit)

    print(f"Найдено книг с аудио: {len(books_with_audio)}")

    # Логируем ID возвращаемых книг
    for book in books_with_audio:
        logging.debug(f"Returning book ID: {book['_id']}")

    return [book_helper(book) for book in books_with_audio]

@router.get("/count-with-audio", response_model=int)
async def count_books_with_audio(db=Depends(get_database)):
    crud_book = get_book_crud(db)
    print("Подсчет всех книг с аудио")

    # Запрос для подсчета всех книг с аудиофайлом
    count = await crud_book.collection.count_documents({
        "audio_file_path": {
            "$exists": True,
            "$nin": ['', 'string'],  # Исключаем пустые строки и 'string'
            "$regex": "^https"  # Проверяем, что путь начинается с 'https'
        }
    })

    print(f"Общее количество аудиокниг: {count}")

    return count

@router.get("/count-last-month", response_model=int)
async def count_books_last_month(db=Depends(get_database)):
    crud_book = get_book_crud(db)
    print("Подсчет книг, добавленных за последний месяц")

    # Получаем дату месяц назад
    one_month_ago = datetime.utcnow() - timedelta(days=30)

    # Подсчитываем книги, у которых `created_at` >= one_month_ago
    count = await crud_book.collection.count_documents({
        "created_at": {"$gte": one_month_ago}
    })

    print(f"Количество книг, добавленных за последний месяц: {count}")

    return count

