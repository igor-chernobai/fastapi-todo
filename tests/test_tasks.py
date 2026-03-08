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


def test_update_task_success(client, get_task_id):
    response = client.put(f'/tasks/{get_task_id}/', json={'title': 'Updated task', 'completed': True})
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == get_task_id

    assert data['title'] == 'Updated task'
    assert data['completed'] is True


def test_update_task_validation_errors(client, get_task_id):
    response = client.put('/tasks/9999/', json={'title': 'Updated task', 'completed': True})
    assert response.status_code == 404

    response = client.put(f'/tasks/{get_task_id}/', json={'title': 'Updated task'})
    assert response.status_code == 422

    response = client.put(f'/tasks/{get_task_id}/', json={'title': ['Not a string'], 'completed': True})
    assert response.status_code == 422


def test_delete_task_success(client, get_task_id):
    response = client.delete(f'/tasks/{get_task_id}')
    assert response.status_code == 200
    assert response.json()['success'] is True

    response = client.get('/tasks/')
    assert len(response.json()) == 0


def test_delete_task_not_found(client):
    response = client.delete('/tasks/99999/')
    assert response.status_code == 404
