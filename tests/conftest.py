import pytest
from fastapi.testclient import TestClient

from app import storage
from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def empty_tasks():
    storage.tasks.clear()


@pytest.fixture
def get_task_id(client):
    res = client.post('/tasks/', json={'title': 'Old task', 'completed': False})
    return res.json()['id']
