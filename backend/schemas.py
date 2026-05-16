"""Pydantic schemas for request/response validation.

The schemas mirror the SQLAlchemy models but are intentionally
simplified – they expose only the fields that are relevant for the API.
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field

# ---------- Resident ----------
class ResidentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    villa_id: Optional[int] = None

class ResidentCreate(ResidentBase):
    pass

class ResidentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    villa_id: Optional[int] = None

class ResidentInDBBase(ResidentBase):
    id: int
    class Config:
        orm_mode = True

class Resident(ResidentInDBBase):
    villa_name: Optional[str] = None
    fees: List["FeeInDB"] = []

# ---------- Villa ----------
class VillaBase(BaseModel):
    name: str
    address: str
    capacity: Optional[int] = Field(default=1)
    is_active: Optional[bool] = Field(default=True)

class VillaCreate(VillaBase):
    pass

class VillaUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    capacity: Optional[int] = None
    is_active: Optional[bool] = None

class VillaInDBBase(VillaBase):
    id: int
    class Config:
        orm_mode = True

class Villa(VillaInDBBase):
    residents: List[ResidentInDBBase] = []

# ---------- Fee ----------
class FeeBase(BaseModel):
    amount: float
    description: Optional[str] = None
    due_date: date
    paid: Optional[bool] = False

class FeeCreate(FeeBase):
    resident_id: int

class FeeUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    paid: Optional[bool] = None

class FeeInDBBase(FeeBase):
    id: int
    resident_id: int
    class Config:
        orm_mode = True

class Fee(FeeInDBBase):
    resident: Optional[ResidentInDBBase] = None

# ---------- Response wrappers ----------
class ResidentList(BaseModel):
    residents: List[Resident]

class VillaList(BaseModel):
    villas: List[Villa]

class FeeList(BaseModel):
    fees: List[Fee]
