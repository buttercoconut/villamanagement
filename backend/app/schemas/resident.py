from pydantic import BaseModel, Field
from typing import Optional

class ResidentBase(BaseModel):
    name: str = Field(..., example="홍길동")
    phone: str = Field(..., example="010-1234-5678")
    address: str = Field(..., example="서울특별시 강남구")
    area_sq_m: float = Field(..., example=45.0)
    resident_type: str = Field(..., example="아파트")

class ResidentCreate(ResidentBase):
    pass

class Resident(ResidentBase):
    id: int
    class Config:
        orm_mode = True
