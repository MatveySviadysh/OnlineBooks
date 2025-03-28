from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId


class UserEmail(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    email: EmailStr

    @validator("id", pre=True, always=True)
    def validate_id(cls, v):
        return str(v) if isinstance(v, ObjectId) else v

    class Config:
        allow_population_by_field_name = True
        orm_mode = True