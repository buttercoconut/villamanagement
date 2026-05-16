"""Entry point for the FastAPI application.

This file is intentionally minimal – it simply imports the FastAPI
application instance from :mod:`app` and runs it with Uvicorn when the
module is executed directly.  The real logic lives in the other
modules.
"""

from fastapi import FastAPI
from app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
