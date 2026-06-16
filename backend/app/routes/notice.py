from fastapi import APIRouter, HTTPException
from typing import List
from app.models.notice import NoticeCreate, NoticeUpdate, NoticeInDB

router = APIRouter()

# In-memory store for demo purposes
notice_db: dict[int, NoticeInDB] = {}
next_id = 1

@router.post("/", response_model=NoticeInDB)
async def create_notice(notice: NoticeCreate):
    global next_id
    notice_obj = NoticeInDB(id=next_id, posted_by="admin", posted_at="2024-01-01T00:00:00Z", **notice.dict())
    notice_db[next_id] = notice_obj
    next_id += 1
    return notice_obj

@router.get("/", response_model=List[NoticeInDB])
async def list_notices():
    return list(notice_db.values())

@router.get("/{notice_id}", response_model=NoticeInDB)
async def get_notice(notice_id: int):
    notice = notice_db.get(notice_id)
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return notice

@router.put("/{notice_id}", response_model=NoticeInDB)
async def update_notice(notice_id: int, notice: NoticeUpdate):
    stored = notice_db.get(notice_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Notice not found")
    updated_data = notice.dict(exclude_unset=True)
    updated_notice = stored.copy(update=updated_data)
    notice_db[notice_id] = updated_notice
    return updated_notice

@router.delete("/{notice_id}")
async def delete_notice(notice_id: int):
    if notice_id not in notice_db:
        raise HTTPException(status_code=404, detail="Notice not found")
    del notice_db[notice_id]
    return {"detail": "Notice deleted"}
