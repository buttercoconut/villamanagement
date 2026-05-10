"""Simple test for villa creation.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.fixture
def villa_payload():
    return {
        "name": "Test Villa",
        "address": "123 Test St",
        "area_sq_m": 200.0,
    }

def test_create_villa(villa_payload):
    response = client.post("/villas/", json=villa_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == villa_payload["name"]
    assert data["address"] == villa_payload["address"]
    assert data["area_sq_m"] == villa_payload["area_sq_m"]

