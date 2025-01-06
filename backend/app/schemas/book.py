from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: Optional[float] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class BookResponse(BookBase):
    id: str = Field(alias="_id")

    class Config:
        from_attributes = True
        populate_by_name = True 