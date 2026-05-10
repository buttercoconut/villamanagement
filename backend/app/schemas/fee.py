from pydantic import BaseModel

class FeeBase(BaseModel):
    resident_id: int
    amount: float
    due_date: str

class FeeCreate(FeeBase):
    pass

class Fee(FeeBase):
    id: int
    paid: bool = False
    class Config:
        orm_mode = True
