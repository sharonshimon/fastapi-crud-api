import pytest
from fastapi.testclient import TestClient

BASE = "/api/v1/users"


def test_list_users_empty(client: TestClient) -> None:
    # No users yet → empty list
    r = client.get(f"{BASE}/")
    assert r.status_code == 200
    assert r.json() == []


def test_post_user_validation_error(client: TestClient) -> None:
    # Missing 'status' field → 422
    r = client.post(f"{BASE}/", json={})
    assert r.status_code == 422

    # Invalid status value → 422
    r2 = client.post(f"{BASE}/", json={"status": "flying"})
    assert r2.status_code == 422


def test_get_user_not_found(client: TestClient) -> None:
    # No such ID → 404
    r = client.get(f"{BASE}/9999")
    assert r.status_code == 404


def test_put_user_validation_and_not_found(client: TestClient) -> None:
    # First create a valid user
    user = client.post(f"{BASE}/", json={"status": "inactive"}).json()

    # Invalid payload → 422
    r_bad = client.put(f"{BASE}/{user['id']}", json={})
    assert r_bad.status_code == 422

    # Non-existent user → 404
    r_missing = client.put(f"{BASE}/9999", json={"status": "active"})
    assert r_missing.status_code == 404


def test_delete_user_not_found(client: TestClient) -> None:
    # Deleting a missing user → 404
    r = client.delete(f"{BASE}/9999")
    assert r.status_code == 404

def test_put_user_success(client: TestClient) -> None:
    # Create a user
    created = client.post(f"{BASE}/", json={"status": "active"}).json()
    user_id = created["id"]

    # Update its status
    r = client.put(f"{BASE}/{user_id}", json={"status": "inactive"})
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == user_id
    assert body["status"] == "inactive"


def test_delete_user_success(client: TestClient) -> None:
    # Create a user
    created = client.post(f"{BASE}/", json={"status": "inactive"}).json()
    user_id = created["id"]

    # Delete it
    r = client.delete(f"{BASE}/{user_id}")
    assert r.status_code == 204

    # Confirm 404 afterwards
    r2 = client.get(f"{BASE}/{user_id}")
    assert r2.status_code == 404