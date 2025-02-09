from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId

class Recommendation(BaseModel):
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    book_ids: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }