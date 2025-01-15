from datetime import datetime
from bson import ObjectId
from schemas.book import BookResponse
from datetime import datetime

def book_helper(book: dict) -> dict:
    """Преобразование документа книги в ответ API"""
    return {
        "_id": str(book["_id"]),
        "title": book.get("title", ""),
        "author": book.get("author", ""),
        "genre": book.get("genre", ""),
        "publication_date": book.get("publication_date", datetime.utcnow()),
        "language": book.get("language", ""),
        "page_count": book.get("page_count", 0),
        "rating": book.get("rating", 0.0),
        "file_url": book["file_url"], 
        "image": book["image"],
        "audio_file_path": book["audio_file_path"],
        "created_at": book.get("created_at", datetime.utcnow()),
        "updated_at": book.get("updated_at", datetime.utcnow())
    }