from urllib.request import HTTPPasswordMgr
from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.cruds import task

import api.schemas.done as d
import api.cruds.done as dc
from api.db import get_db

router = APIRouter()

@router.put("/tasks/{task_id}/done",response_model=d.DoneResponse)
async def mark_task_as_done(task_id:int,db:AsyncSession=Depends(get_db)):
    done = await dc.get_done(db,task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400,detail='Done already exists!')
    return await dc.create_done(db,task_id)

@router.delete("/tasks/{task_id}/done",response_model=d.DoneResponse)
async def unmark_task_as_done(task_id:int,db:AsyncSession=Depends(get_db)):
    done = await dc.get_done(db,task_id=task_id)
    if done is None:
        raise HTTPException(status_code=404,detail='Done not found')
    return await dc.delete_done(db,original=done)


