from typing import List
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId

class Storage(BaseModel):
    user_id: int = Field(..., description="ID of the user who owns this storage")
    book_ids: List[str] = Field(default_factory=list, description="List of favorite book IDs")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }