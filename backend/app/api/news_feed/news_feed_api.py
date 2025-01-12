from fastapi import APIRouter, Depends
from typing import List
from core.config import get_database
from schemas.news_feed import NewsFeedCreate, NewsFeedUpdate, NewsFeedResponse
from crud.crud_news_feed import get_news_feed_crud, CRUDNewsFeed

router = APIRouter(
    prefix="/news_feed",
    tags=["news_feed"],
    responses={404: {"description": "лента новостей пуста или не найдена"}}
)

async def get_crud_news_feed(db=Depends(get_database)):
    return get_news_feed_crud(db)

@router.post("/", response_model=NewsFeedResponse)
async def create_news_feed(news_feed: NewsFeedCreate, crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.create_news_feed(news_feed)
@router.get("/{news_feed_id}", response_model=NewsFeedResponse)
async def read_news_feed(news_feed_id: str, crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.get_news_feed(news_feed_id)

@router.put("/{news_feed_id}", response_model=NewsFeedResponse)
async def update_news_feed(news_feed_id: str, news_feed_update: NewsFeedUpdate, crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.update_news_feed(news_feed_id, news_feed_update)

@router.delete("/{news_feed_id}", response_model=dict)
async def delete_news_feed(news_feed_id: str, crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.delete_news_feed(news_feed_id)

@router.get("/", response_model=List[NewsFeedResponse])
async def list_news_feeds(skip: int = 0, limit: int = 10, crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.list_news_feeds(skip=skip, limit=limit)

@router.delete("/", response_model=dict)
async def delete_all_news_feeds(crud: CRUDNewsFeed = Depends(get_crud_news_feed)):
    return await crud.delete_all_news_feeds()

