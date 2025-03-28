from fastapi import APIRouter
from .user.user_api import router as user_router
from .book.book_api import router as book_router
from .comment.comment_api import router as comment_api
from .mailing_list.mailing_list_api import router as mailing_list_router
from .news_feed.news_feed_api import router as news_feed_router
from .recomend.recomend_api import router as recomend_router
from .children_and_perents.children_and_perents_api import router as children_and_perents_router
from .storage.storage_api import router as storage_router
from .book.book_second import router as book_router2
router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(book_router, prefix="/books", tags=["books"])
router.include_router(comment_api, prefix="/comments", tags=["comments"])
router.include_router(mailing_list_router, prefix="/mailing_list", tags=["mailing_list"])
router.include_router(news_feed_router, prefix="/news_feed", tags=["news_feed"])
router.include_router(recomend_router, prefix="/recomend", tags=["recomend"])
router.include_router(children_and_perents_router, prefix="/children_and_perents", tags=["children_and_perents"])
router.include_router(storage_router, prefix="/storage", tags=["storage"])
router.include_router(book_router2, prefix="/book", tags=["book"])