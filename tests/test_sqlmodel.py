"""
Test cases for the SQLModel FastAPI application.
"""

import os
import pytest
from fastapi.testclient import TestClient

# Set up DATABASE_URL before importing the modules that need it
os.environ["DATABASE_URL"] = "postgresql+asyncpg://test:test@test:5432/test"

from fastapi_playground.sqlmodel.main import app


@pytest.fixture(name="client")
def client_fixture():
    """Create a test client"""
    client = TestClient(app)
    return client


def test_ping_endpoint(client):
    """Test the ping endpoint"""
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


# Placeholder tests - users can expand these with proper database setup
def test_user_database_persistence():
    """Placeholder: Test that users are properly persisted"""
    # TODO: Add tests for database persistence across requests
    # This requires setting up a test database with proper async session handling
    pass


def test_user_validation_sqlmodel():
    """Placeholder: Test SQLModel validation"""
    # TODO: Add tests for SQLModel field validation
    pass


def test_database_relationships():
    """Placeholder: Test database relationships if added"""
    # TODO: Add tests for foreign keys, joins, etc. when models are extended
    pass


def test_create_and_get_users():
    """Placeholder: Test full CRUD operations"""
    # TODO: Implement with proper test database setup
    # This would test POST /songs and GET /songs endpoints
    # Requires async session mocking or test database
    pass
