from datetime import datetime
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True  # Enables ORM mode