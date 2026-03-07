def test_create_task_success(client):
    response = client.post('/tasks/', json={'title': 'Work', 'completed': True})
    data = response.json()

    assert response.status_code == 201
    assert data['title'] == 'Work'
    assert 'id' in data


def test_create_task_validation_errors(client):
    response = client.post('/tasks/', json={})
    assert response.status_code == 422

    response = client.post('/tasks/', json={'title': 122313})
    assert response.status_code == 422


def test_get_tasks_list(client):
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert response.json() == []


def test_get_tasks_list_with_data(client):
    client.post('/tasks/', json={'title': 'Task 1', 'completed': False})
    client.post('/tasks/', json={'title': 'Task 2', 'completed': False})

    response = client.get('/tasks/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2
