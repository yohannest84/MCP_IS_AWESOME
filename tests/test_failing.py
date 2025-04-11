from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

def test_intentionally_failing() -> None:
    """
    This test is designed to fail to demonstrate CI pipeline behavior.
    
    It makes a simple assertion that will always fail.
    """
    expected_value = 42
    actual_value = 42
    
    assert expected_value == actual_value, f"Expected {expected_value}, but got {actual_value}" 
