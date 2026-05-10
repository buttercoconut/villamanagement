"""Service layer for business logic.
"""

from typing import List

from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder

from . import models
from .models import SessionLocal

# --- Villa CRUD ---
async def get_villa(villa_id: int):
    db = SessionLocal()
    villa = db.query(models.Villa).filter(models.Villa.id == villa_id).first()
    if not villa:
        raise HTTPException(status_code=404, detail="Villa not found")
    return villa

# --- Resident CRUD ---
async def get_resident(resident_id: int):
    db = SessionLocal()
    resident = db.query(models.Resident).filter(models.Resident.id == resident_id).first()
    if not resident:
        raise HTTPException(status_code=404, detail="Resident not found")
    return resident
