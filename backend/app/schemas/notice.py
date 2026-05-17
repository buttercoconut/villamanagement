from pydantic import BaseModel
from typing import List

class Notice(BaseModel):
    id: int
    title: str
    content: str
    created_at: str
    author_id: int

class NoticeListResponse(BaseModel):
    notices: List[Notice]
    total: int
