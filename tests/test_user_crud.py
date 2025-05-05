from typing import Optional

import pytest
from sqlalchemy.orm import Session

from app.crud.user_crud import (
    create_user,
    delete_user,
    get_user,
    update_user,
)


def test_create_and_get_user(db_session: Session) -> None:
    """
    GIVEN a clean database
    WHEN create_user is called with status 'active'
    THEN the returned UserTable has an id and correct status,
         and get_user can retrieve it.
    """
    new_user = create_user(db_session, status="active")
    assert new_user.id is not None
    assert new_user.status == "active"

    fetched = get_user(db_session, new_user.id)
    assert fetched is not None
    assert fetched.id == new_user.id
    assert fetched.status == "active"


@pytest.mark.parametrize(
    ("initial_status", "new_status"),
    [("active", "inactive"), ("inactive", "active")],
)
def test_update_user_status(
    db_session: Session,
    initial_status: str,
    new_status: str,
) -> None:
    """
    Test that update_user toggles the status correctly
    and returns None when the user does not exist.
    """
    user = create_user(db_session, status=initial_status)

    updated = update_user(db_session, user.id, new_status)
    assert updated is not None
    assert updated.status == new_status

    missing = update_user(db_session, user_id=9999, status="active")
    assert missing is None


def test_delete_user(db_session: Session) -> None:
    """
    Test that delete_user returns True on first delete
    and False if the user is already removed.
    """
    user = create_user(db_session, status="active")

    result_first = delete_user(db_session, user.id)
    assert result_first is True

    result_second = delete_user(db_session, user.id)
    assert result_second is False
