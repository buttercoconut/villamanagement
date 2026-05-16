"""SQLAlchemy models for the villa management system.

- :class:`Resident` – a person living in a villa.
- :class:`Villa` – a property that can have many residents.
- :class:`Fee` – a fee record for a resident (e.g. rent, utilities).
"""

from datetime import date
from typing import Optional

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

from database import Base

class Villa(Base):
    __tablename__ = "villas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    capacity = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)

    residents = relationship("Resident", back_populates="villa", cascade="all, delete-orphan")

class Resident(Base):
    __tablename__ = "residents"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    villa_id = Column(Integer, ForeignKey("villas.id"))

    villa = relationship("Villa", back_populates="residents")
    fees = relationship("Fee", back_populates="resident", cascade="all, delete-orphan")

class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    resident_id = Column(Integer, ForeignKey("residents.id"))
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(Date, nullable=False)
    paid = Column(Boolean, default=False)

    resident = relationship("Resident", back_populates="fees")
