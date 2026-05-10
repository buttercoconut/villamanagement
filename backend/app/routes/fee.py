from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.fee import Fee, FeeCreate

router = APIRouter()

_fees: List[Fee] = []
_next_id = 1

@router.post("/", response_model=Fee)
async def create_fee(fee: FeeCreate):
    global _next_id
    new_fee = Fee(id=_next_id, **fee.dict())
    _fees.append(new_fee)
    _next_id += 1
    return new_fee

@router.get("/", response_model=List[Fee])
async def list_fees():
    return _fees
