from fastapi import FastAPI

from app import storage
from app.schemas import TaskCreate, TaskResponse
from app.services import create_task, update_task

app = FastAPI()


@app.get('/tasks', tags=['Tasks'])
def get_tasks() -> list[TaskResponse]:
    """
    Returns a list of all task objects.
    """
    return list(storage.tasks.values())


@app.post('/tasks', tags=['Tasks'])
def add_task(task: TaskCreate) -> TaskResponse:
    """
    Create a new task and return the created task object.
    """

    return create_task(task)


@app.put('/tasks/{task_id}', tags=['Tasks'])
def update_task_view(task_id: int, task_data: TaskCreate):
    """
    Update a task by ID and return the updated task.
    """
    return update_task(task_id, task_data)
