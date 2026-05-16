"""Database configuration and base model.

Uses SQLAlchemy 2.0 style with declarative base.
"""

from __future__ import annotations

from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import Settings

settings = Settings()

# SQLite database in the project directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL = settings.database_url or f"sqlite:///{BASE_DIR / 'app.db'}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for path operation functions

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
