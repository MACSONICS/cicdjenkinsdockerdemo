import pytest
import calc_server
from calc_server import app

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_add(client):
    """Test the multiply route with valid input."""
    response = client.get('/add/3/4')
    assert response.status_code == 200
    assert response.json == {"result": 7}
