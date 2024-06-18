from contextlib import asynccontextmanager
from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: Optional[str]


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Записать это видео")
#     return {"data": task}
