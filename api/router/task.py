from typing import List

from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.cruds.task as tc
import api.schemas.task as ts

router = APIRouter()

@router.get('/tasks',response_model=List[ts.Task])
async def list_tasks(db:AsyncSession = Depends(get_db)):
    return await tc.get_tasks_with_done(db)

@router.post('/tasks',response_model=ts.TaskCreateResponse)
async def create_task(task_body:ts.TaskCreate,db:AsyncSession=Depends(get_db)):
    return await tc.create_task(db,task_body)

@router.put('/tasks/{task_id}',response_model=ts.TaskCreateResponse)
async def update_task(task_id:int,task_body:ts.TaskCreate,db:AsyncSession=Depends(get_db)):
    task = await tc.get_task(db,task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404,detail='Task not found!!')
    return await tc.update_task(db,task_body,original=task)

@router.delete('/tasks/{tasks_id}',response_model=None)
async def delete_task(task_id:int,db:AsyncSession=Depends(get_db)):
    task = await tc.get_task(db,task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404,detail='Task not found!!')
    return await tc.delete_task(db,original=task)

