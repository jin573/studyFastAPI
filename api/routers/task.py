from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_crud
import api.schemas.task as task_schema
from api.db import get_db

router = APIRouter()

"""@router.get("/tasks")
async def list_tasks():
    pass
"""
@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks(db:AsyncSession=Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)

"""@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db:Session = Depends(get_db)): #의존성 주입
    return task_crud.create_task(db, task_body)"""
@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db:AsyncSession = Depends(get_db)): #의존성 주입
    return await task_crud.create_task(db, task_body) #task_crud의 create_task에서 await 사용하므로 라우팅시에도 await 사용하여야 함

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate, db:AsyncSession=Depends(get_db)):
    task=await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found") #예외를 발생
    return await task_crud.update_task(db, task_body, original=task)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db:AsyncSession=Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task_crud.delete_task(db, original=task)