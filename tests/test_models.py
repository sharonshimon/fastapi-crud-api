# tests/test_schemas.py

import pytest
from pydantic import ValidationError

from app.models import User, Partner


@pytest.mark.parametrize(
    "input_data, expected_status",
    [
        ({"status": "active"}, "active"),
        ({"status": "inactive"}, "inactive"),
    ],
)
def test_user_schema_valid(input_data, expected_status):
    user = User(**input_data)
    assert user.status == expected_status
    assert user.id is None  # ID is optional on create


@pytest.mark.parametrize(
    "input_data",
    [
        {},                         # missing status
        {"status": "unknown"},      # invalid literal
        {"status": 123},            # wrong type
    ],
)
def test_user_schema_invalid(input_data):
    with pytest.raises(ValidationError):
        User(**input_data)


@pytest.mark.parametrize(
    "payload",
    [
        ({"foo": "bar", "nums": [1, 2, 3]}),
    ],
)
def test_partner_schema_valid(payload):
    p = Partner(data=payload)
    assert p.data == payload
    assert p.id is None


@pytest.mark.parametrize(
    "input_data",
    [
        {},                 # missing data
        {"data": "string"}, # not a dict
        {"data": [1,2,3]},  # list instead of dict
    ],
)
def test_partner_schema_invalid(input_data):
    with pytest.raises(ValidationError):
        Partner(**input_data)
