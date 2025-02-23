
from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class StorageBase(BaseModel):
    """Base model for Storage"""
    user_id: int = Field(..., description="ID of the user who owns this storage")
    book_ids: List[str] = Field(default_factory=list, description="List of favorite book IDs")

class StorageCreate(StorageBase):
    """Model for creating new storage"""
    pass  # Inherits all fields from StorageBase

class StorageUpdate(BaseModel):
    """Model for updating storage"""
    user_id: Optional[int] = None
    book_ids: Optional[List[str]] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class StorageResponse(StorageBase):
    """Model for client response"""
    id: str = Field(..., alias="_id") 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {
            ObjectId: str  # Proper serialization of ObjectId
        }
