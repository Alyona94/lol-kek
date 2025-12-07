import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    return client

 
def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0


