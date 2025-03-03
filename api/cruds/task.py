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