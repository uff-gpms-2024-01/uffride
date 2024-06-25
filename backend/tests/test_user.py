from .testconf import client

def test_create_user(client):
    response = client.post("/api/user/register", json={
        "name": "Test",
        "email": "email@test.com.br",
        "password": "123456789"
    })

    assert response.status_code == 201

def test_should_not_create_user(client):
    response = client.post("/api/user/register", json={
        "name": "Test",
        "email": "email@test.com.br",
        "password": "123456789"
    })

    assert response.status_code == 500

def test_login_user(client):
    response = client.post("/api/user/login", json={
        "email": "email@test.com.br",
        "password": "123456789"
    })

    assert response.status_code == 200	 