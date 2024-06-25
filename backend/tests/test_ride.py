
from .testconf import client

def test_get_ride(client):
    response = client.get("/api/ride/1")
    assert response.status_code == 200

def test_get_current_rides(client):
    response = client.get("/api/ride/current")
    assert response.status_code == 200

def test_get_all_rides(client):
    response = client.get("/api/rides")
    assert response.status_code == 200

def test_post_ride(client):
    response = client.post("/api/ride", json={
        "where_address": "Rua A",
        "where_lat": 0,
        "where_long": 0,
        "to_where_address": "Rua B",
        "to_where_lat": 0,
        "to_where_long": 0,
        "driver": 1,
        "vehicle_id": 1
    })

    assert response.status_code == 200

def test_put_ride(client):
    response = client.put("/api/ride/1")
    assert response.status_code == 200

def test_delete_ride(client):
    response = client.delete("/api/ride/1")
    assert response.status_code == 200