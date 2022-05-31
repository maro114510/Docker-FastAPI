from inspect import CO_ASYNC_GENERATOR
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    """タスク自体の呼び出し"""
    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True)
    title = Column(String(1024))

    done = relationship('Done',back_populates='task')

class Done(Base):
    """タスクの実行環境の呼び出し"""
    __tablename__ = 'dones'

    id = Column(Integer,ForeignKey('tasks.id'),primary_key=True)

    task = relationship('Task',back_populates='done')