"""
Pytest configuration and shared fixtures for the test suite.
"""

import pytest
from sqlmodel import Session, create_engine
from sqlmodel.pool import StaticPool

from fastapi_playground.sqlmodel.models import SQLModel


@pytest.fixture(scope="session")
def test_engine():
    """Create a test database engine for the session"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def test_session(test_engine):
    """Create a fresh test database session for each test"""
    with Session(test_engine) as session:
        yield session
        session.rollback()


# Placeholder fixtures - users can add more as needed
@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {"first_name": "Test", "last_name": "User", "middle_name": "Sample", "age": 30}


@pytest.fixture
def sample_users_data():
    """Multiple sample users for testing"""
    return [
        {"first_name": "Alice", "last_name": "Johnson", "middle_name": "Marie", "age": 28},
        {"first_name": "Bob", "last_name": "Smith", "middle_name": "William", "age": 35},
        {"first_name": "Carol", "last_name": "Davis", "middle_name": "Ann", "age": 42},
    ]


# TODO: Add more fixtures as the application grows
# Examples:
# - Authentication fixtures
# - Mock external service fixtures
# - Test data factories
# - Database seeding fixtures
