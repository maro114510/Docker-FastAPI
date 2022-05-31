from typing import Tuple,Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as tm


async def get_done(db:AsyncSession,task_id:int)->Optional[tm.Done]:
    result:Result = await db.execute(
        select(tm.Done).filter(tm.Done.id==task_id)
    )
    done:Optional[Tuple[tm.Done]] = result.first()
    return done[0] if done is not None else None

async def create_done(db:AsyncSession,task_id:int)->tm.Done:
    done = tm.Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done

async def delete_done(db:AsyncSession,original:tm.Done)->None:
    await db.delete(original)
    await db.commit()

