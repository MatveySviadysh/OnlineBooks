from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class ChildrenAndPerents(BaseModel):
    book_ids: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None