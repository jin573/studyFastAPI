#Fat Controller 를 피하기 위해 CRUD Controller 분리
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db:Session, task_create:task_schema.TaskCreate) -> task_model.Task: #반환 타입 힌트
    task = task_model.Task(**task_create.dict())#**으로 키 값 가져오기
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks_with_done(db:Session) -> list[tuple[int, str, bool]]:
    result:Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done"), #done.id가 존재하면 done=True로, 아니면 False
        ).outerjoin(task_model.Done)
    )
    return result.all()

#result 객체는 여러 튜플로 반환된다.
#하지만 select로는 Task라는 테이블 자체를 반환하게 되므로 
#scalars로 값 자체를 반환
def get_task(db:Session, task_id:int) -> task_model.Task|None:
    result:Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id==task_id)
    )
    return result.scalars().first()

def update_task(db:Session, task_create:task_schema.TaskCreate, original:task_model.Task)->task_model.Task:
    original.title=task_create.title
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def delete_task(db:Session, original:task_model.Task) -> None:
    db.delete(original)
    db.commit()
