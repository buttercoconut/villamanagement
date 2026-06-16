from fastapi import FastAPI
from app.routes import resident, notice, fee

app = FastAPI(title="Villa Management System API")

# Include routers
app.include_router(resident.router, prefix="/api/residents", tags=["Residents"])
app.include_router(notice.router, prefix="/api/notices", tags=["Notices"])
app.include_router(fee.router, prefix="/api/fees", tags=["Fees"])

@app.get("/")
async def root():
    return {"message": "Welcome to Villa Management System API"}
