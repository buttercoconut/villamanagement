from fastapi import FastAPI
from .routes import notice

app = FastAPI(title="Villa Management API")
app.include_router(notice.router)
