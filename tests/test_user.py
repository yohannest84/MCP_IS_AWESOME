from typing import TYPE_CHECKING

import pytest
from src.models.user import User

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_user_creation() -> None:
    """Test basic user creation with valid data."""
    user = User(
        username="testuser",
        email="test@example.com",
        password="password123"
    )
    
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == "password123"

def test_user_string_representation() -> None:
    """Test the string representation of a User object."""
    user = User(
        username="testuser",
        email="test@example.com",
        password="password123"
    )
    
    assert str(user) == "<User testuser>"
    assert repr(user) == "<User testuser>" 