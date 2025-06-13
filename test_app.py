import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Contact Us" in response.data

def test_form_submission(client):
    response = client.post('/', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Hello from test!'
    })
    assert response.status_code == 200
    assert b"Thank you for your submission" in response.data
