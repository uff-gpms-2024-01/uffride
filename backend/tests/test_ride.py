def test_ride(client):
    response = client.get("/api/rides")
    assert response.status_code == 200
    response = client.post("/api/ride", json={"id": 1, "driver": 1, "vehicle_id": 1, "status": "ongoing"})
    assert response.status_code == 200
    response = client.get("/api/ride/1")
    assert response.status_code == 200
    response = client.put("/api/ride/1")
    assert response.status_code == 200
    response = client.delete("/api/ride/1")
    assert response.status_code == 200