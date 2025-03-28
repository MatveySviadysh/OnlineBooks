from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ChildrenAndParentsBase(BaseModel):
    book_ids: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ChildrenAndParentsCreate(ChildrenAndParentsBase):
    pass


class ChildrenAndParentsUpdate(BaseModel):
    book_ids: Optional[List[str]] = Field(default_factory=list)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class ChildrenAndParentsResponse(ChildrenAndParentsBase):
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
