from typing import TYPE_CHECKING

import pytest
from src.models.user import User

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_user_validation_fails() -> None:
    """
    Test that demonstrates a failing user validation.
    
    This test is designed to fail to show how CI blocks merges.
    """
    # Create a user with invalid email
    user = User(
        username="test_user",
        email="invalid-email",  # This should fail validation
        password="secure123"
    )
    
    # This assertion will fail because the email is invalid
    assert user.is_valid(), "Expected user to be valid, but validation failed" 