def get_token(client):
    client.post("/api/auth/register", json={"name":"Admin","email":"admin@example.com","password":"pw"})
    # set admin flag directly via DB (quick for tests)
    from ..database import SessionLocal
    from .. import crud, models, auth as auth_module
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.email=="admin@example.com").first()
    user.is_admin = True
    db.add(user)
    db.commit()
    db.close()
    r = client.post("/api/auth/login", json={"email":"admin@example.com","password":"pw"})
    return r.json()["access_token"]

def test_crud_sweets_and_purchase(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    # create sweet
    r = client.post("/api/sweets", json={"name":"Gulab Jamun","category":"Indian","price":10.5,"quantity":5}, headers=headers)
    assert r.status_code == 201
    sweet = r.json()
    sid = sweet["id"]
    # purchase 2
    r2 = client.post(f"/api/sweets/{sid}/purchase", json={"quantity":2}, headers=headers)
    assert r2.status_code == 200
    assert r2.json()["quantity"] == 3
    # restock 5 (admin)
    r3 = client.post(f"/api/sweets/{sid}/restock", json={"quantity":5}, headers=headers)
    assert r3.status_code == 200
    assert r3.json()["quantity"] == 8
    # delete (admin)
    r4 = client.delete(f"/api/sweets/{sid}", headers=headers)
    assert r4.status_code == 204
