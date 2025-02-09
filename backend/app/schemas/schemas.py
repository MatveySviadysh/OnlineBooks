from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    recommendation_id: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    recommendation_id: Optional[str] = None  # ID рекомендации

    class Config:
        json_encoders = {
            ObjectId: str  # Для корректной сериализации ObjectId в JSON
        }