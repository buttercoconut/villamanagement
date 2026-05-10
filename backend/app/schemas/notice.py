from pydantic import BaseModel
from typing import List

class NoticeBase(BaseModel):
    title: str
    content: str

class NoticeCreate(NoticeBase):
    pass

class Notice(NoticeBase):
    id: int
    created_at: str
    class Config:
        orm_mode = True
