def test_get_domain(client):
    res = client.get("/domains/pets")
    data = res.json
    assert res.status_code == 200
    assert data.get("name") == "pets"
    assert data.get("password") is None
