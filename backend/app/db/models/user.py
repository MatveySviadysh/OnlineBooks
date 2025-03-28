from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    username: str
    email: str
    password: str
    recommendation_id: Optional[str] = None  # ID рекомендации
    storage_id: Optional[str] = None 

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str  # Для корректной сериализации ObjectId в JSON
        }