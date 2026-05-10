"""Database models using SQLAlchemy.

We use a SQLite database for simplicity. In production you would swap
the engine URL.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Villa(Base):
    __tablename__ = "villains"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    area_sq_m = Column(Float, nullable=False)
    residents = relationship("Resident", back_populates="villa")

class Resident(Base):
    __tablename__ = "residents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    move_in_date = Column(Date, default=datetime.utcnow)
    villa_id = Column(Integer, ForeignKey("villains.id"))
    villa = relationship("Villa", back_populates="residents")

# SQLite for dev
DATABASE_URL = "sqlite:///./villa.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
