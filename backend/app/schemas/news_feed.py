from pydantic import BaseModel, Field, constr
from bson import ObjectId
from datetime import datetime
from typing import Optional


class NewsFeedBase(BaseModel):
    title: constr(min_length=1)
    content: str
    image_url: str


class NewsFeedCreate(NewsFeedBase):
    pass


class NewsFeedUpdate(BaseModel):
    title: Optional[constr(min_length=1)]
    content: Optional[str]
    image_url: Optional[str]


class NewsFeedResponse(NewsFeedBase):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
