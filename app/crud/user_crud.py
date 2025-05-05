from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session

from ..models import UserTable

def get_all_users(db: Session) -> List[UserTable]:
    """
    Retrieve all users from the database.

    Args:
        db: database session

    Returns:
        A list of UserTable instances.
    """
    return db.query(UserTable).all()


def create_user(db: Session, status: str) -> UserTable:
    """
    Create and persist a new user.

    Args:
        db: database session
        status: must be "active" or "inactive"

    Returns:
        The newly created UserTable instance.
    """
    user = UserTable(status=status)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> Optional[UserTable]:
    """
    Retrieve a user by ID.

    Args:
        db: database session
        user_id: primary key of the user

    Returns:
        The UserTable instance or None if not found.
    """
    return db.query(UserTable).filter(UserTable.id == user_id).first()


def update_user(
    db: Session,
    user_id: int,
    status: str,
) -> Optional[UserTable]:
    """
    Update an existing user's status.

    Args:
        db: database session
        user_id: primary key of the user
        status: new status to set

    Returns:
        The updated UserTable instance or None if not found.
    """
    user = get_user(db, user_id)
    if user is None:
        return None

    user.status = status
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> bool:
    """
    Delete a user by ID.

    Args:
        db: database session
        user_id: primary key of the user

    Returns:
        True if deleted, False if no user was found.
    """
    user = get_user(db, user_id)
    if user is None:
        return False

    db.delete(user)
    db.commit()
    return True

