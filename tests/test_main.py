import pytest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == "Hello World"
    assert data['version'] == "1.0.0"
    assert 'timestamp' in data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == "healthy"
    assert data['service'] == "myapp"

def test_info_endpoint(client):
    response = client.get('/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['app'] == "MyPythonApp"
    assert data['version'] == "1.0.0"