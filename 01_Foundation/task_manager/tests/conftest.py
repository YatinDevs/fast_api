import pytest
from fastapi.testclient import TestClient
from ..main import app  # Relative import

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client