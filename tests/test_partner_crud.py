
import pytest
from sqlalchemy.orm import Session

from app.crud.partner_crud import (
    list_partners,
    create_partner,
    get_partner,
    update_partner,
    delete_partner,
)


def test_list_partners_empty(db_session: Session) -> None:
    assert list_partners(db_session) == []


def test_create_and_list_and_get_partner(db_session: Session) -> None:
    payload = {"foo": "bar", "nums": [1, 2]}
    created = create_partner(db_session, payload)
    assert "id" in created and isinstance(created["id"], int)
    assert created["data"] == payload

    all_partners = list_partners(db_session)
    assert isinstance(all_partners, list)
    assert any(
        p["id"] == created["id"] and p["data"] == payload
        for p in all_partners
    )

    fetched = get_partner(db_session, created["id"])
    assert fetched == created


def test_get_partner_not_found(db_session: Session) -> None:
    assert get_partner(db_session, 9999) is None


def test_update_partner_success_and_failure(db_session: Session) -> None:
    initial = {"a": 1}
    updated_data = {"a": 2}

    created = create_partner(db_session, initial)
    updated = update_partner(db_session, created["id"], updated_data)
    assert updated is not None
    assert updated["id"] == created["id"]
    assert updated["data"] == updated_data

    assert update_partner(db_session, 9999, {}) is None


def test_delete_partner_success_and_failure(db_session: Session) -> None:
    payload = {"x": "y"}
    created = create_partner(db_session, payload)

    first_delete = delete_partner(db_session, created["id"])
    assert first_delete is True

    assert get_partner(db_session, created["id"]) is None

    second_delete = delete_partner(db_session, created["id"])
    assert second_delete is False
