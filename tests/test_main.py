"""
Test cases for the main FastAPI application.
"""

from fastapi.testclient import TestClient

from fastapi_playground.main import app

client = TestClient(app)


def test_create_user():
    """Test creating a user via POST /users/"""
    user_data = {"firstName": "John", "lastName": "Doe", "age": 30}

    response = client.post("/users/", json=user_data)

    assert response.status_code == 200
    data = response.json()
    # The response should use camelCase due to alias_generator
    assert data["firstName"] == "John"
    assert data["lastName"] == "Doe"
    assert data["age"] == 30


def test_docs_endpoint():
    """Test that the docs endpoint is accessible"""
    response = client.get("/")
    assert response.status_code == 200
    assert "swagger" in response.text.lower() or "openapi" in response.text.lower()


# Placeholder tests - users can expand these
def test_user_validation():
    """Placeholder: Test user input validation"""
    # TODO: Add tests for invalid user data
    pass


def test_user_edge_cases():
    """Placeholder: Test edge cases for user creation"""
    # TODO: Add tests for edge cases like empty strings, negative ages, etc.
    pass
