import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_chatbot_response():
    response = client.post(
        "/api/v1/chatbot/",
        json={"message": "Hello, chatbot!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)
