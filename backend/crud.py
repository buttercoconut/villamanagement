"""CRUD helper functions.

These functions are intentionally thin wrappers around SQLAlchemy
operations.  They keep the routers clean and make unit‑testing easier.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from models import Resident, Villa, Fee
from schemas import ResidentCreate, ResidentUpdate, VillaCreate, VillaUpdate, FeeCreate, FeeUpdate

# ---------- Residents ----------

def get_resident(db: Session, resident_id: int) -> Optional[Resident]:
    return db.query(Resident).filter(Resident.id == resident_id).first()


def get_residents(db: Session, skip: int = 0, limit: int = 100) -> List[Resident]:
    return db.query(Resident).offset(skip).limit(limit).all()


def create_resident(db: Session, resident_in: ResidentCreate) -> Resident:
    resident = Resident(**resident_in.dict())
    db.add(resident)
    db.commit()
    db.refresh(resident)
    return resident


def update_resident(db: Session, resident_id: int, resident_in: ResidentUpdate) -> Optional[Resident]:
    resident = get_resident(db, resident_id)
    if not resident:
        return None
    for field, value in resident_in.dict(exclude_unset=True).items():
        setattr(resident, field, value)
    db.commit()
    db.refresh(resident)
    return resident


def delete_resident(db: Session, resident_id: int) -> bool:
    resident = get_resident(db, resident_id)
    if not resident:
        return False
    db.delete(resident)
    db.commit()
    return True

# ---------- Villas ----------

def get_villa(db: Session, villa_id: int) -> Optional[Villa]:
    return db.query(Villa).filter(Villa.id == villa_id).first()


def get_villas(db: Session, skip: int = 0, limit: int = 100) -> List[Villa]:
    return db.query(Villa).offset(skip).limit(limit).all()


def create_villa(db: Session, villa_in: VillaCreate) -> Villa:
    villa = Villa(**villa_in.dict())
    db.add(villa)
    db.commit()
    db.refresh(villa)
    return villa


def update_villa(db: Session, villa_id: int, villa_in: VillaUpdate) -> Optional[Villa]:
    villa = get_villa(db, villa_id)
    if not villa:
        return None
    for field, value in villa_in.dict(exclude_unset=True).items():
        setattr(villa, field, value)
    db.commit()
    db.refresh(villa)
    return villa


def delete_villa(db: Session, villa_id: int) -> bool:
    villa = get_villa(db, villa_id)
    if not villa:
        return False
    db.delete(villa)
    db.commit()
    return True

# ---------- Fees ----------

def get_fee(db: Session, fee_id: int) -> Optional[Fee]:
    return db.query(Fee).filter(Fee.id == fee_id).first()


def get_fees(db: Session, resident_id: Optional[int] = None, skip: int = 0, limit: int = 100) -> List[Fee]:
    query = db.query(Fee)
    if resident_id is not None:
        query = query.filter(Fee.resident_id == resident_id)
    return query.offset(skip).limit(limit).all()


def create_fee(db: Session, fee_in: FeeCreate) -> Fee:
    fee = Fee(**fee_in.dict())
    db.add(fee)
    db.commit()
    db.refresh(fee)
    return fee


def update_fee(db: Session, fee_id: int, fee_in: FeeUpdate) -> Optional[Fee]:
    fee = get_fee(db, fee_id)
    if not fee:
        return None
    for field, value in fee_in.dict(exclude_unset=True).items():
        setattr(fee, field, value)
    db.commit()
    db.refresh(fee)
    return fee


def delete_fee(db: Session, fee_id: int) -> bool:
    fee = get_fee(db, fee_id)
    if not fee:
        return False
    db.delete(fee)
    db.commit()
    return True
