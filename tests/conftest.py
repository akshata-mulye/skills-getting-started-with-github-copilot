import pytest
from fastapi.testclient import TestClient
from src.app import app, activities
import copy

@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to known state before each test"""
    # Deep copy of the original state
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
