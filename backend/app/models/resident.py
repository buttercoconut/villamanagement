from pydantic import BaseModel, Field
from typing import Optional

class Resident(BaseModel):
    id: int = Field(..., description="Unique resident identifier")
    name: str = Field(..., description="Resident full name")
    phone: str = Field(..., description="Contact phone number")
    address: str = Field(..., description="Residential address")
    area_sq_m: float = Field(..., description="Living area in square meters")
    resident_type: str = Field(..., description="Type of resident (e.g., owner, renter)")
    fee_info: Optional[dict] = Field(None, description="Calculated fee details")
