from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .user import User


class Comment(BaseModel):
    user: User
    text: str = Field(..., max_length=1000)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None