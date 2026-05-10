from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.resident import Resident, ResidentCreate

router = APIRouter()

# In-memory store for demo purposes
_residents: List[Resident] = []
_next_id = 1

@router.post("/", response_model=Resident)
async def create_resident(resident: ResidentCreate):
    global _next_id
    new_resident = Resident(id=_next_id, **resident.dict())
    _residents.append(new_resident)
    _next_id += 1
    return new_resident

@router.get("/", response_model=List[Resident])
async def list_residents():
    return _residents
