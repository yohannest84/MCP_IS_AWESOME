"""Test module for API routes.

This module contains test cases for verifying the functionality
of the Flask application's HTTP endpoints.
"""
from typing import TYPE_CHECKING
from flask.testing import FlaskClient

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_index_route(client: FlaskClient) -> None:
    """Test the index route returns successful response.

    This test verifies that the main index route '/' is accessible
    and returns a 200 OK status code, indicating the application
    is properly handling root requests.

    Args:
        client: Flask test client fixture for making HTTP requests.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client: FlaskClient) -> None:
    """Test the health check endpoint returns correct response.

    This test ensures that the health check endpoint '/health' is working
    and returns both a 200 OK status code and the expected JSON response.
    This endpoint is crucial for monitoring and load balancing systems.

    Args:
        client: Flask test client fixture for making HTTP requests.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}