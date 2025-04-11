"""Test module for API routes.

This module contains test cases for verifying the functionality
of the Flask application's HTTP endpoints. All tests are designed
to be independent and should pass in CI environment.
"""
from typing import TYPE_CHECKING
from flask.testing import FlaskClient

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_index_route(client: FlaskClient) -> None:
    """Test the index route returns successful response.

    This test ensures that the application's root endpoint is
    properly configured and responding with success status.

    Args:
        client: Flask test client fixture for making HTTP requests.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client: FlaskClient) -> None:
    """Test the health check endpoint returns correct response.

    This test verifies that the health check endpoint is working
    correctly by checking both the status code and response content.
    A passing test indicates the application is healthy and ready
    to handle requests.

    Args:
        client: Flask test client fixture for making HTTP requests.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}