from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import api.cruds.task as task_crud
import api.schemas.task as task_schema
from api.db import get_db

router = APIRouter()

"""@router.get("/tasks")
async def list_tasks():
    pass
"""
@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks(db:Session=Depends(get_db)):
    return task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db:Session = Depends(get_db)): #의존성 주입
    return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate, db:Session=Depends(get_db)):
    task=task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found") #예외를 발생

    return task_crud.update_task(db, task_body, original=task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return