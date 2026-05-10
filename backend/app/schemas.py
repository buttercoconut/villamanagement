"""Pydantic schemas for request/response validation.
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field

# --- Villa schemas ---
class VillaBase(BaseModel):
    name: str = Field(..., example="Sea View")
    address: str = Field(..., example="123 Ocean Drive")
    area_sq_m: float = Field(..., example=250.0)

class VillaCreate(VillaBase):
    pass

class VillaUpdate(VillaBase):
    pass

class VillaInDB(VillaBase):
    id: int
    residents: List["ResidentInDB"] = []

    class Config:
        orm_mode = True

# --- Resident schemas ---
class ResidentBase(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, example=30)
    move_in_date: Optional[date] = Field(None, example="2023-01-15")

class ResidentCreate(ResidentBase):
    villa_id: int

class ResidentUpdate(ResidentBase):
    pass

class ResidentInDB(ResidentBase):
    id: int
    villa_id: int

    class Config:
        orm_mode = True

# --- Response wrappers ---
class VillaListResponse(BaseModel):
    villas: List[VillaInDB]

class ResidentListResponse(BaseModel):
    residents: List[ResidentInDB]

# Forward references
VillaInDB.update_forward_refs()
