from typing import List, Optional
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from schemas.comment import CommentCreate, CommentUpdate, CommentResponse

class CRUDComment:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.comments


    async def create_comment(self, comment: CommentCreate) -> CommentResponse:
        comment_dict = comment.dict()
        result = await self.collection.insert_one(comment_dict)
        comment_dict["_id"] = str(result.inserted_id)
        return CommentResponse(**comment_dict)


    async def get_comment(self, comment_id: str) -> CommentResponse:
        try:
            comment = await self.collection.find_one({"_id": ObjectId(comment_id)})
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid comment ID format")

        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")

        comment["_id"] = str(comment["_id"])
        return CommentResponse(**comment)

    async def update_comment(self, comment_id: str, comment_update: CommentUpdate) -> CommentResponse:
        try:
            update_data = comment_update.dict(exclude_unset=True)
            result = await self.collection.update_one({"_id": ObjectId(comment_id)}, {"$set": update_data})

            if result.modified_count == 0:
                raise HTTPException(status_code=404, detail="Comment not found or no changes made")

            updated_comment = await self.collection.find_one({"_id": ObjectId(comment_id)})
            updated_comment["_id"] = str(updated_comment["_id"])
            return CommentResponse(**updated_comment)
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid comment ID format")

    async def delete_comment(self, comment_id: str) -> dict:
        try:
            result = await self.collection.delete_one({"_id": ObjectId(comment_id)})

            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail="Comment not found")

            return {"detail": "Comment deleted successfully"}
        except InvalidId:
            raise HTTPException(status_code=400, detail="Invalid comment ID format")

    async def list_comments(self, skip: int = 0, limit: int = 10) -> List[CommentResponse]:
        comments = []
        async for comment in self.collection.find().skip(skip).limit(limit):
            comment["_id"] = str(comment["_id"])
            comments.append(CommentResponse(**comment))
        
        return comments

def get_comment_crud(db: AsyncIOMotorDatabase) -> CRUDComment:
    return CRUDComment(db)
