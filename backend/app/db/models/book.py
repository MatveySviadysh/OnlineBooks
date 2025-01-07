from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(..., max_length=200, unique=True)
    author: str = Field(..., max_length=100)
    description: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    publication_date: Optional[datetime] = None
    genre: Optional[str] = None
    language: Optional[str] = None
    rating: Optional[float] = None
    page_count: Optional[int] = None
    isbn: str = Field(..., unique=True)
    publisher: Optional[str] = None
    dimensions: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True