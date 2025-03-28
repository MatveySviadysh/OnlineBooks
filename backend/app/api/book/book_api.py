from fastapi import APIRouter, Depends
from typing import List
from core.config import get_database
from schemas.book import BookCreate, BookUpdate, BookResponse
from crud.crud_book import get_book_crud
from api.book.helper_book import book_helper

router = APIRouter(
    prefix="/books", 
    tags=["books"],
    responses={404: {"description": "Книга не найдена"}}
)

@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.create(book)

@router.get("/content/{book_id}", response_model=str)
async def get_book_content(book_id: str, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    book = await crud_book.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    file_url = book.get("file_url")
    if file_url is None:
        raise HTTPException(status_code=404, detail="URL файла не найден")
    content = await crud_book.get_file_content(file_url)
    return content


@router.get("/search", response_model=List[BookResponse])
async def search_books(query: str, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.search_books(query)

@router.put("/{book_id}/rating", response_model=BookResponse)
async def update_book_rating(book_id: str, rating: float, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.update_rating(book_id, rating)

@router.get("/", response_model=List[BookResponse])
async def get_all_books(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_all(skip, limit)

@router.get("/popular", response_model=List[BookResponse])
async def get_popular_books(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_popular(skip, limit)

@router.get("/recent", response_model=List[BookResponse])
async def get_recent_books(skip: int = 0, limit: int = 100, db = Depends(get_database)):
    """Получение недавно опубликованных книг (не старше 1 года)"""
    crud_book = get_book_crud(db)
    return await crud_book.get_recent(skip, limit)

@router.get("/all", response_model=List[BookResponse]) 
async def get_all_books_without_limit(db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_all_without_limit()

@router.get("/count", response_model=int)
async def get_books_count(db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_count()

@router.get("/average_rating", response_model=float)
async def get_average_rating(db = Depends(get_database)):
    crud_book = get_book_crud(db)
    return await crud_book.get_average_rating()
    
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

@router.get("/genre/{genre}", response_model=List[BookResponse])
async def get_books_by_genre(
    genre: str, 
    skip: int = 0, 
    limit: int = 100, 
    db = Depends(get_database)
):
    """Получение всех книг определенного жанра"""
    crud_book = get_book_crud(db)
    return await crud_book.get_by_genre(genre, skip, limit)

