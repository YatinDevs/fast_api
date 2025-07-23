from fastapi import APIRouter
from app.api.v1.endpoints import tasks  # Absolute import

router = APIRouter()
router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])