from fastapi import FastAPI

from app.storage import tasks

app = FastAPI()


@app.get('/tasks', tags=['Tasks'])
def get_tasks():
    """
    Returns a list of all task objects.
    """
    return list(tasks.values())
