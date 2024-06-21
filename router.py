from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи", ],
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
