"""FastAPI application factory.

The :data:`app` object is created here and all routers are included.
The configuration is loaded from :mod:`config`.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import residents, villas, fees
from config import Settings

settings = Settings()

app = FastAPI(
    title="Villa Management API",
    description="API for managing residents, villas and fee calculations.",
    version="0.1.0",
)

# Allow CORS for local development – adjust origins in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(residents.router, prefix="/residents", tags=["Residents"])
app.include_router(villas.router, prefix="/villas", tags=["Villas"])
app.include_router(fees.router, prefix="/fees", tags=["Fees"])

# Dependency to get DB session
from database import SessionLocal

@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response
