from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item_success():
    response = client.post("/api/v1/items/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"name": "Router Wi-Fi", "category": "Networking", "sku": "INV-FST-001", "initial_stock": 10})
    assert response.status_code == 201

def test_create_item_unauthorized():
    response = client.post("/api/v1/items/", json={"name": "Router Wi-Fi", "category": "Networking", "sku": "INV-FST-001", "initial_stock": 10})
    assert response.status_code == 401

def test_create_item_invalid_sku():
    response = client.post("/api/v1/items/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"name": "Router Wi-Fi", "category": "Networking", "sku": "SALAH-001"})
    assert response.status_code == 422

def test_get_all_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_not_found():
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404

def test_delete_item_unauthorized():
    response = client.delete("/api/v1/items/1")
    assert response.status_code == 401

def test_delete_item_success():
    client.post("/api/v1/items/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"name": "Kabel LAN", "category": "Networking", "sku": "INV-FST-002", "initial_stock": 5})
    response = client.delete("/api/v1/items/1", headers={"X-API-Key": "gudang-rahasia-2026"})
    assert response.status_code == 204

def test_setup_item_for_transaction():
    res = client.post("/api/v1/items/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"name": "Kertas HVS", "category": "Office", "sku": "INV-FST-003", "initial_stock": 50})
    assert res.status_code == 201

def test_transaction_in_success():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 2, "quantity": 20, "type": "IN"})
    assert res.status_code == 201

def test_transaction_out_success():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 2, "quantity": 10, "type": "OUT"})
    assert res.status_code == 201

def test_transaction_out_insufficient_stock():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 2, "quantity": 999, "type": "OUT"})
    assert res.status_code == 400

def test_transaction_invalid_type():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 2, "quantity": 10, "type": "PINJAM"})
    assert res.status_code == 422

def test_transaction_invalid_quantity():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 2, "quantity": -5, "type": "IN"})
    assert res.status_code == 422

def test_transaction_item_not_found():
    res = client.post("/api/v1/transactions/", headers={"X-API-Key": "gudang-rahasia-2026"}, json={"item_id": 999, "quantity": 10, "type": "IN"})
    assert res.status_code == 404

def test_transaction_unauthorized():
    res = client.post("/api/v1/transactions/", json={"item_id": 2, "quantity": 10, "type": "IN"})
    assert res.status_code == 401
