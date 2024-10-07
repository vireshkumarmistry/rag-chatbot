import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_file_upload():
    pdf_path = os.path.join(os.path.dirname(__file__), '../../', 'ZIGUP-FY24-Results-Deck.pdf')

    assert os.path.exists(pdf_path), "Test PDF file not found at the given path"

    with open(pdf_path, 'rb') as pdf_file:
        files = {
            "file": ("ZIGUP-FY24-Results-Deck.pdf", pdf_file, "application/pdf")
        }

        response = client.post("/api/v1/upload/", files=files)

        assert response.status_code == 200
        assert response.json()[
                   "message"] == "Document 'ZIGUP-FY24-Results-Deck.pdf' has been successfully uploaded and processed."