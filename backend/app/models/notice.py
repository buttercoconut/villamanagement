from pydantic import BaseModel, Field
from typing import Optional

class NoticeBase(BaseModel):
    title: str = Field(..., example="정기 점검 안내")
    content: str = Field(..., example="다음 주 금요일에 전기 점검이 예정되어 있습니다.")
    posted_at: Optional[str] = None

class NoticeCreate(NoticeBase):
    pass

class NoticeUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class NoticeInDB(NoticeBase):
    id: int
    posted_by: str
    posted_at: str

    class Config:
        orm_mode = True
