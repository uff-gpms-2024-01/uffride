import pytest
from .testconf import client

def test_get_ride(client):
    response = client.get("/api/rides")
    assert response.status_code == 200