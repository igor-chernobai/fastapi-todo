from app.schemas import TaskCreate, TaskResponse
from app import storage


def create_task(task: TaskCreate) -> TaskResponse:
    task_dict = task.model_dump()
    task_dict.update({'id': storage.task_id})

    storage.tasks[storage.task_id] = task_dict
    storage.task_id += 1

    return TaskResponse(**task_dict)
