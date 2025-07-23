# In app/api/v1/__init__.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/tasks/")
def temp():
    return {"message": "Temporary route"}