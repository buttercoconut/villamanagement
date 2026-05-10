from fastapi import FastAPI
from app.routes import resident, notice, fee

app = FastAPI(title="Villa Management API")

app.include_router(resident.router, prefix="/residents", tags=["Residents"])
app.include_router(notice.router, prefix="/notices", tags=["Notices"])
app.include_router(fee.router, prefix="/fees", tags=["Fees"])

@app.get("/")
async def root():
    return {"message": "Welcome to Villa Management API"}
