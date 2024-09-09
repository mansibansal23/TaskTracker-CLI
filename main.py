from fastapi import FastAPI, Depends, HTTPException
from database import get_db, Base, engine
from sqlalchemy.orm import Session
from models import Task, Status
from schemas import CreateTask, TaskUpdate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def get_task(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.post("/create")
async def create_task(task: CreateTask, db: Session = Depends(get_db)):
    task = Task(**task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"message": "task created successfully"}


@app.delete("/delete/{task_id}")
async def delete(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    db.delete(task)
    db.commit()
    return {"Message": f"Task with id: {task_id} deleted successfully"}


@app.patch("/update/{task_id}")
async def update_task(task_id: int, task_update: TaskUpdate,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_update.task_title is not None:
        task.task_title = task_update.task_title

    if task_update.task_description is not None:
        task.task_description = task_update.task_description

    if task_update.status is not None:
        task.status = task_update.status
    print(task)
    db.commit()
    db.refresh(task)

    return {"Message": "Update Done"}
