import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []


def test_add_task(client):
    task = {'title': 'Test Task'}
    response = client.post('/tasks', data=json.dumps(task), content_type='application/json')
    assert response.status_code == 201
    assert response.json == task


def test_delete_task(client):
    # task = {'title': 'Test Task'}
    # client.post('/tasks', data=json.dumps(task), content_type='application/json')

    response = client.delete('/tasks/0')
    assert response.status_code == 204

    response = client.get('/tasks')
    assert response.json == []