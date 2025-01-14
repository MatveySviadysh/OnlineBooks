from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., max_length=200, unique=True)
    author: str = Field(..., max_length=100)
    genre: str
    publication_date: datetime
    language: str
    page_count: int
    rating: float = Field(default=1.0, ge=1.0, le=5.0)
    file_url: str 
    image: str


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    genre: str | None = None
    publication_date: datetime | None = None
    language: str | None = None
    page_count: int | None = None
    rating: float | None = Field(default=None, ge=1.0, le=5.0)

class BookResponse(BookBase):
    id: str = Field(alias="_id")
    file_url: str 
    image: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: dt.strftime("%d-%m-%Y")
        }