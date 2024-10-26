import pytest
from fastapi.testclient import TestClient
from api.main import app
from api.schemas import QueryRequest, QueryResponse

client = TestClient(app)

@pytest.mark.parametrize(
    "model, query, expected_status_code",
    [
        ("text-davinci-003", "What is the meaning of life?", 200),
        ("text-curie-001", "Translate 'Hello world!' to Spanish", 200),
        ("code-davinci-002", "Write a Python function to reverse a string", 200),
        ("text-ada-001", "Summarize the following article", 200),
        ("text-babbage-001", "Generate a creative story about a cat", 200),
        ("text-davinci-002", "Invalid Model", 400),  # Test for invalid model
        ("text-davinci-003", "", 400),  # Test for empty query
    ],
)
def test_query_endpoint(model, query, expected_status_code):
    query_request = QueryRequest(model=model, query=query)
    response = client.post("/query", json=query_request.dict())
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        assert response.json() == QueryResponse(id=1, model=model, query=query, response="").dict()
    elif expected_status_code == 400:
        assert "error" in response.json()

def test_auth_endpoint():
    response = client.post("/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_auth_endpoint_invalid_credentials():
    response = client.post("/token", data={"username": "invaliduser", "password": "invalidpassword"})
    assert response.status_code == 401
    assert "detail" in response.json()