from fastapi import APIRouter
from .user.user_api import router as user_router
from .book.book_api import router as book_router
from .comment.comment_api import router as comment_api
from .mailing_list.mailing_list_api import router as mailing_list_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(book_router, prefix="/books", tags=["books"])
router.include_router(comment_api, prefix="/comments", tags=["comments"])
router.include_router(mailing_list_router, prefix="/mailing_list", tags=["mailing_list"])