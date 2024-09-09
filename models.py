from database import Base
from sqlalchemy import Column, String, Integer, Enum
from enum import Enum as PyEnum


class Status(str, PyEnum):
    todo = "To Do"
    in_progress = "In Progress"
    done = "Done"


class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    task_title = Column(String, index=True)
    task_description = Column(String, nullable=False)
    status = Column(Enum(Status), default=Status.todo)


