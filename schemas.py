from typing import Optional

from pydantic import BaseModel


class CreateTask(BaseModel):
    task_title: str
    task_description: str
    status: Optional[str] = "To Do"

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    task_title: Optional[str] = None
    task_description: Optional[str] = None
    status: Optional[str] = "To Do"

    class Config:
        from_attributes = True