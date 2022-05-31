from typing import Optional

from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title:Optional[str] = Field(None,example='oppai')

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskBase):
    id:int

    class Config:
        orm_mode=True

class Task(TaskBase):
    id:int
    done:bool = Field(False,description='完了')

    class Config:
        orm_mode=True