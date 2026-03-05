from fastapi import FastAPI

app = FastAPI()

tasks_list = [
    {
        'id': 1,
        'title': 'My first task',
        'completed': False
    }
]


@app.get('/tasks', tags=['Tasks'])
def get_tasks():
    """
    Returns a list of all task objects.
    """
    return tasks_list
