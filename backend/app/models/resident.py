from pydantic import BaseModel, Field
from typing import Optional

class ResidentBase(BaseModel):
    name: str = Field(..., example="홍길동")
    phone: str = Field(..., example="010-1234-5678")
    address: str = Field(..., example="서울시 강남구 테헤란로 123")
    area_sq_m: float = Field(..., example=45.0)
    resident_type: str = Field(..., example="아파트")  # e.g., 아파트, 빌라, 단독주택

class ResidentCreate(ResidentBase):
    pass

class ResidentUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    area_sq_m: Optional[float] = None
    resident_type: Optional[str] = None

class ResidentInDB(ResidentBase):
    id: int
    fee_due: float = 0.0

    class Config:
        orm_mode = True
