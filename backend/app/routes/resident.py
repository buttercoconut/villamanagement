from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.resident import ResidentCreate, ResidentUpdate, ResidentInDB
from app.services.resident_service import ResidentService

router = APIRouter()

# In-memory store for demo purposes
resident_db: dict[int, ResidentInDB] = {}
next_id = 1

@router.post("/", response_model=ResidentInDB)
async def create_resident(resident: ResidentCreate):
    global next_id
    resident_obj = ResidentInDB(id=next_id, **resident.dict(), fee_due=0.0)
    resident_db[next_id] = resident_obj
    next_id += 1
    return resident_obj

@router.get("/", response_model=List[ResidentInDB])
async def list_residents():
    return list(resident_db.values())

@router.get("/{resident_id}", response_model=ResidentInDB)
async def get_resident(resident_id: int):
    resident = resident_db.get(resident_id)
    if not resident:
        raise HTTPException(status_code=404, detail="Resident not found")
    return resident

@router.put("/{resident_id}", response_model=ResidentInDB)
async def update_resident(resident_id: int, resident: ResidentUpdate):
    stored = resident_db.get(resident_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Resident not found")
    updated_data = resident.dict(exclude_unset=True)
    updated_resident = stored.copy(update=updated_data)
    resident_db[resident_id] = updated_resident
    return updated_resident

@router.delete("/{resident_id}")
async def delete_resident(resident_id: int):
    if resident_id not in resident_db:
        raise HTTPException(status_code=404, detail="Resident not found")
    del resident_db[resident_id]
    return {"detail": "Resident deleted"}
