from typing import List
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from schemas.news_feed import NewsFeedCreate, NewsFeedUpdate, NewsFeedResponse
from datetime import datetime
import httpx

class CRUDNewsFeed:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.news_feed

    
    async def create_news_feed(self, news_feed: NewsFeedCreate) -> NewsFeedResponse:
        news_feed_dict = news_feed.dict()
        news_feed_dict["created_at"] = datetime.utcnow().isoformat()
        news_feed_dict["updated_at"] = datetime.utcnow().isoformat()
        result = await self.collection.insert_one(news_feed_dict)
        news_feed_dict["_id"] = str(result.inserted_id)

        await self.send_notification(news_feed_dict["title"])
        return NewsFeedResponse(**news_feed_dict)

    async def send_notification(self, post_title: str):
        url = "http://127.0.0.1:8888/newsletter"
        message = f'Пост с названием "{post_title}" доступен теперь.'
        async with httpx.AsyncClient() as client:
            await client.post(url, json={"message": message})

    async def get_news_feed(self, news_feed_id: str) -> NewsFeedResponse:
        try:
            news_feed = await self.collection.find_one({"_id": ObjectId(news_feed_id)})
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid news feed ID format")

        if news_feed is None:
            raise HTTPException(status_code=404, detail="News feed not found")

        news_feed["_id"] = str(news_feed["_id"])
        return NewsFeedResponse(**news_feed)

    async def update_news_feed(self, news_feed_id: str, news_feed_update: NewsFeedUpdate) -> NewsFeedResponse:
        try:
            update_data = news_feed_update.dict(exclude_unset=True)
            if update_data:
                update_data["updated_at"] = datetime.utcnow().isoformat()
                result = await self.collection.update_one({"_id": ObjectId(news_feed_id)}, {"$set": update_data})

                if result.modified_count == 0:
                    raise HTTPException(status_code=404, detail="News feed not found or no changes made")

            updated_news_feed = await self.collection.find_one({"_id": ObjectId(news_feed_id)})
            updated_news_feed["_id"] = str(updated_news_feed["_id"])
            return NewsFeedResponse(**updated_news_feed)
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid news feed ID format")

    async def delete_news_feed(self, news_feed_id: str) -> dict:
        try:
            result = await self.collection.delete_one({"_id": ObjectId(news_feed_id)})

            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail="News feed not found")

            return {"detail": "News feed deleted successfully"}
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid news feed ID format")

    async def list_news_feeds(self, skip: int = 0, limit: int = 10) -> List[NewsFeedResponse]:
        news_feeds = []
        async for news_feed in self.collection.find().skip(skip).limit(limit):
            news_feed["_id"] = str(news_feed["_id"])
            news_feeds.append(NewsFeedResponse(**news_feed))
        return news_feeds

    async def delete_all_news_feeds(self) -> dict:
        result = await self.collection.delete_many({})
        return {"detail": f"{result.deleted_count} news feeds deleted successfully"}

def get_news_feed_crud(db: AsyncIOMotorDatabase) -> CRUDNewsFeed:
    return CRUDNewsFeed(db)
