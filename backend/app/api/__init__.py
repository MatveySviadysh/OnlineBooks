from fastapi import APIRouter
from .user.user_api import router as user_router
from .book.book_api import router as book_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(book_router, prefix="/books", tags=["books"])
