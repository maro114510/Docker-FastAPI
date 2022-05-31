from fastapi import FastAPI

from api.router import task,done

app = FastAPI()

app.include_router(task.router)
app.include_router(done.router)
