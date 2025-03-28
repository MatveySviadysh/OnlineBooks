from typing import List, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class RecommendationBase(BaseModel):
    """Базовая модель для Recommendation"""
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    book_ids: List[str] = Field(default_factory=list)

class RecommendationCreate(RecommendationBase):
    """Модель для создания новой рекомендации"""
    pass  # Наследует все поля от RecommendationBase

class RecommendationUpdate(BaseModel):
    """Модель для обновления рекомендации"""
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    book_ids: Optional[List[str]] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class RecommendationResponse(RecommendationBase):
    """Модель для возврата клиенту"""
    id: str = Field(..., alias="_id")  # MongoDB ObjectId
    book_ids: List[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str  # Корректная сериализация ObjectId
        }
