"""Routes for villa endpoints.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .. import models, schemas, services

villa_router = APIRouter()

# Create villa
@villa_router.post("/", response_model=schemas.VillaInDB, status_code=status.HTTP_201_CREATED)
async def create_villa(villa: schemas.VillaCreate):
    db = models.SessionLocal()
    db_villa = models.Villa(**villa.dict())
    db.add(db_villa)
    db.commit()
    db.refresh(db_villa)
    return db_villa

# List villas
@villa_router.get("/", response_model=schemas.VillaListResponse)
async def list_villas():
    db = models.SessionLocal()
    villas = db.query(models.Villa).all()
    return schemas.VillaListResponse(villas=villas)

# Get villa by id
@villa_router.get("/{villa_id}", response_model=schemas.VillaInDB)
async def get_villa(villa_id: int):
    return await services.get_villa(villa_id)

# Update villa
@villa_router.put("/{villa_id}", response_model=schemas.VillaInDB)
async def update_villa(villa_id: int, villa: schemas.VillaUpdate):
    db = models.SessionLocal()
    db_villa = await services.get_villa(villa_id)
    for key, value in villa.dict(exclude_unset=True).items():
        setattr(db_villa, key, value)
    db.commit()
    db.refresh(db_villa)
    return db_villa

# Delete villa
@villa_router.delete("/{villa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_villa(villa_id: int):
    db = models.SessionLocal()
    db_villa = await services.get_villa(villa_id)
    db.delete(db_villa)
    db.commit()
    return None
