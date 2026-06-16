from fastapi import APIRouter, HTTPException
from typing import List
from app.models.fee import FeeCreate, FeeUpdate, FeeInDB

router = APIRouter()

# In-memory store for demo purposes
fee_db: dict[int, FeeInDB] = {}
next_id = 1

@router.post("/", response_model=FeeInDB)
async def create_fee(fee: FeeCreate):
    global next_id
    total_due = fee.base_fee + fee.area_fee_per_sq_m * fee.area_fee_per_sq_m + fee.usage_fee
    fee_obj = FeeInDB(id=next_id, resident_id=fee.resident_id, total_due=total_due, **fee.dict())
    fee_db[next_id] = fee_obj
    next_id += 1
    return fee_obj

@router.get("/", response_model=List[FeeInDB])
async def list_fees():
    return list(fee_db.values())

@router.get("/{fee_id}", response_model=FeeInDB)
async def get_fee(fee_id: int):
    fee = fee_db.get(fee_id)
    if not fee:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee

@router.put("/{fee_id}", response_model=FeeInDB)
async def update_fee(fee_id: int, fee: FeeUpdate):
    stored = fee_db.get(fee_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Fee not found")
    updated_data = fee.dict(exclude_unset=True)
    updated_fee = stored.copy(update=updated_data)
    fee_db[fee_id] = updated_fee
    return updated_fee

@router.delete("/{fee_id}")
async def delete_fee(fee_id: int):
    if fee_id not in fee_db:
        raise HTTPException(status_code=404, detail="Fee not found")
    del fee_db[fee_id]
    return {"detail": "Fee deleted"}
