"""FastAPI application entry point.

This module creates the FastAPI app, includes routers, and configures
middleware such as CORS and exception handlers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.villa import villa_router
from .routes.resident import resident_router

# Create FastAPI app
app = FastAPI(
    title="Villa Management API",
    description="API for managing villas, residents, and fee calculations.",
    version="0.1.0",
)

# Allow CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(villa_router, prefix="/villas", tags=["Villas"])
app.include_router(resident_router, prefix="/residents", tags=["Residents"])

# Root endpoint
@app.get("/", tags=["Health"])
async def root():
    return {"message": "Villa Management API is running."}
