"""Routes for resident endpoints.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from .. import models, schemas, services

resident_router = APIRouter()

# Create resident
@resident_router.post("/", response_model=schemas.ResidentInDB, status_code=status.HTTP_201_CREATED)
async def create_resident(resident: schemas.ResidentCreate):
    db = models.SessionLocal()
    db_resident = models.Resident(**resident.dict())
    db.add(db_resident)
    db.commit()
    db.refresh(db_resident)
    return db_resident

# List residents
@resident_router.get("/", response_model=schemas.ResidentListResponse)
async def list_residents():
    db = models.SessionLocal()
    residents = db.query(models.Resident).all()
    return schemas.ResidentListResponse(residents=residents)

# Get resident by id
@resident_router.get("/{resident_id}", response_model=schemas.ResidentInDB)
async def get_resident(resident_id: int):
    return await services.get_resident(resident_id)

# Update resident
@resident_router.put("/{resident_id}", response_model=schemas.ResidentInDB)
async def update_resident(resident_id: int, resident: schemas.ResidentUpdate):
    db = models.SessionLocal()
    db_resident = await services.get_resident(resident_id)
    for key, value in resident.dict(exclude_unset=True).items():
        setattr(db_resident, key, value)
    db.commit()
    db.refresh(db_resident)
    return db_resident

# Delete resident
@resident_router.delete("/{resident_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resident(resident_id: int):
    db = models.SessionLocal()
    db_resident = await services.get_resident(resident_id)
    db.delete(db_resident)
    db.commit()
    return None
