from typing import Generator
import pytest
from flask import Flask
from src.app import create_app, db

@pytest.fixture
def app() -> Generator[Flask, None, None]:
    """Create and configure a Flask application for testing.

    Yields:
        Flask: Configured Flask application instance.
    """
    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = 'test-key'

    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app: Flask):
    """Create a test client for the Flask application.

    Args:
        app: Flask application fixture.

    Returns:
        FlaskClient: Test client for making requests.
    """
    return app.test_client() 