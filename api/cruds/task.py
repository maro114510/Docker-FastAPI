from typing import List,Tuple,Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as tm
import api.schemas.task as ts

async def create_task(
    db:AsyncSession,task_create:ts.TaskCreate
)->tm.Task:
    task = tm.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_tasks_with_done(db:AsyncSession)->List[Tuple[int,str,bool]]:
    result:Result = await(
        db.execute(
            select(
                tm.Task.id,
                tm.Task.title,
                tm.Done.id.isnot(None).label('done'),
            ).outerjoin(tm.Done)
        )
    )
    return result.all()

async def get_task(db:AsyncSession,task_id:int)->Optional[tm.Task]:
    result : Result = await db.execute(
        select(tm.Task).filter(tm.Task.id==task_id)
    )
    task:Optional[Tuple[tm.Task]]=result.first()
    return task[0] if task is not None else None

async def update_task(db:AsyncSession,task_create:ts.TaskCreate,original:tm.Task)->tm.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_task(db:AsyncSession,original:tm.Task)->None:
    await db.delete(original)
    await db.commit()

