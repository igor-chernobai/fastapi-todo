from fastapi import HTTPException

from app import storage
from app.schemas import TaskCreate, TaskResponse


def create_task(task: TaskCreate) -> TaskResponse:
    task_dict = task.model_dump()
    task_dict.update({'id': storage.task_id})

    storage.tasks[storage.task_id] = task_dict
    storage.task_id += 1

    return task_dict


def update_task(task_id: int, task_data: TaskCreate):
    if task_id not in storage.tasks:
        raise HTTPException(status_code=404, detail='Task not found')

    updated_task_dict = {'id': task_id, **task_data.model_dump()}
    storage.tasks[task_id] = updated_task_dict

    return updated_task_dict


def delete_task(task_id: int):
    if task_id not in storage.tasks:
        raise HTTPException(status_code=404, detail='Task not found')

    del storage.tasks[task_id]

    return {"success": True}
