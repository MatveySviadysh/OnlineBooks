from pydantic import BaseModel, Field, constr, validator
from bson import ObjectId
from datetime import datetime


class NewsFeed(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    title: constr(min_length=1)
    content: str
    image_url: str
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    @validator("id", pre=True, always=True)
    def validate_id(cls, v):
        return str(v) if isinstance(v, ObjectId) else v

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
