from fastapi import APIRouter

from app import storage
from app.schemas import TaskCreate, TaskResponse
from app.services.tasks import update_task, delete_task, create_task

task_router = APIRouter(prefix='/tasks', tags=['Tasks'])


@task_router.get('/')
def get_tasks() -> list[TaskResponse]:
    """
    Returns a list of all task objects.
    """
    return list(storage.tasks.values())


@task_router.post('/', status_code=201)
def create_task_view(task: TaskCreate) -> TaskResponse:
    """
    Create a new task and return the created task object.
    """
    return create_task(task)


@task_router.put('/{task_id}')
def update_task_view(task_id: int, task_data: TaskCreate):
    """
    Update a task by ID and return the updated task.
    """
    return update_task(task_id, task_data)


@task_router.delete('/{task_id}')
def delete_task_view(task_id: int):
    """
    Delete a task by ID
    """
    return delete_task(task_id)
