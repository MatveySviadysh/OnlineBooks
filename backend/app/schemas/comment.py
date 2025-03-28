from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class CommentBase(BaseModel):
    user_id: Optional[str] = None
    text: str = Field(..., max_length=1000)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    text: Optional[str] = Field(None, max_length=1000)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class CommentResponse(CommentBase):
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True  # Активирует режим ORM для совместимости с SQLAlchemy или другими ORM
