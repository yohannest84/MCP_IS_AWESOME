from typing import TYPE_CHECKING
from flask.testing import FlaskClient

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_index_route(client: FlaskClient) -> None:
    """Test the index route returns successful response.
    
    This test verifies that the main index route '/' is accessible
    and returns a 200 OK status code.

    Args:
        client: Flask test client fixture.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client: FlaskClient) -> None:
    """Test the health check endpoint returns correct response.
    
    This test ensures that the health check endpoint '/health' is working
    and returns both a 200 OK status code and the expected JSON response.

    Args:
        client: Flask test client fixture.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}