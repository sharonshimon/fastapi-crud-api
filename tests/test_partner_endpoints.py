

import pytest
from fastapi.testclient import TestClient

BASE = "/api/v1/partners"


def test_create_list_get_and_delete_partner(client: TestClient) -> None:
    r1 = client.post(f"{BASE}/", json={"data": {"foo": "bar"}})
    assert r1.status_code == 201
    partner = r1.json()
    partner_id = partner["id"]
    assert partner["data"] == {"foo": "bar"}

    r2 = client.get(f"{BASE}/")
    assert r2.status_code == 200
    assert any(p["id"] == partner_id for p in r2.json())

    r3 = client.get(f"{BASE}/{partner_id}")
    assert r3.status_code == 200
    assert r3.json()["data"] == {"foo": "bar"}

    r4 = client.put(f"{BASE}/{partner_id}", json={"data": {"baz": 123}})
    assert r4.status_code == 200
    assert r4.json()["data"] == {"baz": 123}

    r5 = client.delete(f"{BASE}/{partner_id}")
    assert r5.status_code == 204

    r6 = client.get(f"{BASE}/{partner_id}")
    assert r6.status_code == 404


def test_validation_and_not_found(client: TestClient) -> None:
    r1 = client.post(f"{BASE}/", json={})
    assert r1.status_code == 422

    seed = client.post(f"{BASE}/", json={"data": {"x": "y"}}).json()
    r2 = client.put(f"{BASE}/{seed['id']}", json={"foo": "bar"})
    assert r2.status_code == 422

    r3 = client.put(f"{BASE}/9999", json={"data": {"a": 1}})
    assert r3.status_code == 404

    r4 = client.delete(f"{BASE}/9999")
    assert r4.status_code == 404


@pytest.mark.parametrize(
    "method,path",
    [
        ("put",    f"{BASE}/"),
        ("delete", f"{BASE}/"),
        ("post",   f"{BASE}/1"),
    ],
)
def test_partner_methods_not_allowed(client: TestClient, method: str, path: str) -> None:
    response = getattr(client, method)(path)
    assert response.status_code == 405
