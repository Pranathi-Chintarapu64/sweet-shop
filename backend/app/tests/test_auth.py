def test_register_and_login(client):
    # register
    r = client.post("/api/auth/register", json={"name":"Test","email":"t@example.com","password":"secret"})
    assert r.status_code == 201
    data = r.json()
    assert data["email"] == "t@example.com"
    # login
    r2 = client.post("/api/auth/login", json={"email":"t@example.com","password":"secret"})
    assert r2.status_code == 200
    token = r2.json().get("access_token")
    assert token is not None
