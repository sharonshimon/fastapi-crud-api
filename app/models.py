from typing import Any, Dict, Optional
from typing_extensions import Literal

from pydantic import BaseModel,ConfigDict
from sqlalchemy import Column, Integer, String, Text

from .db import Base



class UserTable(Base):
    """
    SQLAlchemy model for the users table.
    """
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    status = Column(
        String,
        nullable=False,
    )


class PartnerTable(Base):
    """
    SQLAlchemy model for the partners table.
    Stores arbitrary JSON as text.
    """
    __tablename__ = "partners"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    data = Column(
        Text,
        nullable=False,
    )




class User(BaseModel):
    """
    Pydantic schema for User.

    - `id` is omitted on create.
    - `status` must be "active" or "inactive".
    """
    id: Optional[int] = None
    status: Literal["active", "inactive"]

    model_config = ConfigDict(from_attributes=True)


class Partner(BaseModel):
    """
    Pydantic schema for Partner.

    - `id` is omitted on create.
    - `data` accepts any JSON-serializable payload.
    """
    id: Optional[int] = None
    data: Dict[str, Any]

    model_config = ConfigDict(from_attributes=True)
