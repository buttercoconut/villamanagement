from pydantic import BaseModel, Field
from typing import Optional

class FeeBase(BaseModel):
    resident_id: int
    base_fee: float = Field(..., example=200000.0)
    area_fee_per_sq_m: float = Field(..., example=5000.0)
    usage_fee: float = Field(..., example=15000.0)
    total_due: Optional[float] = None

class FeeCreate(FeeBase):
    pass

class FeeUpdate(BaseModel):
    base_fee: Optional[float] = None
    area_fee_per_sq_m: Optional[float] = None
    usage_fee: Optional[float] = None

class FeeInDB(FeeBase):
    id: int
    resident_id: int
    total_due: float

    class Config:
        orm_mode = True
