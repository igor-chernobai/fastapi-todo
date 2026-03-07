from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_task_success():
    response = client.post('/tasks/', json={'title': 'Work', 'completed': True})
    data = response.json()

    assert response.status_code == 201
    assert data['title'] == 'Work'
    assert 'id' in data

