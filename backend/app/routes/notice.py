from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.notice import Notice, NoticeListResponse

router = APIRouter(prefix="/notices", tags=["Notices"])

# Dummy in-memory store
_notices = [
    Notice(id=1, title="Welcome", content="Welcome to the villa", created_at="2024-01-01T10:00:00Z", author_id=1),
    Notice(id=2, title="Maintenance", content="Maintenance on Jan 5", created_at="2024-01-02T12:00:00Z", author_id=1),
]

@router.get("/", response_model=NoticeListResponse)
async def list_notices() -> NoticeListResponse:
    return NoticeListResponse(notices=_notices, total=len(_notices))
