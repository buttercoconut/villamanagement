from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.notice import Notice, NoticeCreate

router = APIRouter()

_notices: List[Notice] = []
_next_id = 1

@router.post("/", response_model=Notice)
async def create_notice(notice: NoticeCreate):
    global _next_id
    new_notice = Notice(id=_next_id, created_at="2024-01-01T00:00:00Z", **notice.dict())
    _notices.append(new_notice)
    _next_id += 1
    return new_notice

@router.get("/", response_model=List[Notice])
async def list_notices():
    return _notices
