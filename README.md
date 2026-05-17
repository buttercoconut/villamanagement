# README.md
# Villa Management System

## Backend
- FastAPI
- Docker
- API for notices

## Frontend
- Vue 3 + Vite
- Docker
- Displays notice list and detail

## Running
```bash
# Backend
cd backend
docker build -t villa-backend .
docker run -p 8000:8000 villa-backend

# Frontend
cd frontend
docker build -t villa-frontend .
docker run -p 5173:5173 villa-frontend
```
