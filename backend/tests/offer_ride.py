import pytest
from .testconf import client

def test_offer_ride(client):
    response = client.post("/api/ride/offer", json={
        "where_address": "Rua A",
        "where_lat": 0,
        "where_long": 0,
        "to_where_address": "Rua B",
        "to_where_lat": 0,
        "to_where_long": 0,
        "driver": "João",
        "vehicle_id": 1
    })

    assert response.status_code == 200