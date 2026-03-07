from fastapi import FastAPI

from app import storage
from app.schemas import TaskCreate, TaskResponse
from app.services import create_task

app = FastAPI()


@app.get('/tasks',
         response_model=list[TaskResponse],
         tags=['Tasks'])
def get_tasks() -> list[TaskResponse]:
    """
    Returns a list of all task objects.
    """
    return list(storage.tasks.values())


@app.post('/tasks',
          response_model=TaskResponse,
          tags=['Tasks'])
def add_task(task: TaskCreate) -> TaskResponse:
    """
    Create a new task and return the created task object.
    """

    return create_task(task)
