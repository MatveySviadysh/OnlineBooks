from bson import ObjectId
from schemas.book import BookResponse

def book_helper(book: dict) -> BookResponse:
    return BookResponse(
        id=str(book["_id"]),
        title=book.get("title", ""),
        author=book.get("author", ""),
        description=book.get("description", ""),
        price=book.get("price", 0.0),
        cover_image=book.get("cover_image", ""),
        file_path=book.get("file_path", ""),
        created_at=book.get("created_at"),
        updated_at=book.get("updated_at")
    )