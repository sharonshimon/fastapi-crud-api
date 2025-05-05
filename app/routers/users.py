
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..crud import user_crud

from .. import db, models

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get(
    "/",
    response_model=List[models.User],
)
def read_users(session: Session = Depends(db.get_db)) -> List[models.User]:
    """
    Retrieve all users.
    Returns a list of users. If no users are found, returns an empty list.
    Returns a list of users.
    """
    return user_crud.get_all_users(session)

@router.post(
    "/",
    response_model=models.User,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: models.User,
    session: Session = Depends(db.get_db),
) -> models.User:
    """
    Create a new user.

    Expects JSON body: {"status": "active"/"inactive"}.
    """
    return user_crud.create_user(session, user_in.status)


@router.get(
    "/{user_id}",
    response_model=models.User,
)
def read_user(
    user_id: int,
    session: Session = Depends(db.get_db),
) -> models.User:
    """
    Retrieve a user by its ID.

    Raises 404 if not found.
    """
    user = user_crud.get_user(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={user_id} not found",
        )
    return user


@router.put(
    "/{user_id}",
    response_model=models.User,
)
def update_user(
    user_id: int,
    user_in: models.User,
    session: Session = Depends(db.get_db),
) -> models.User:
    """
    Update an existing user's status.

    Expects JSON body: {"status": "inactive"/"active"}.
    Raises 404 if not found.
    """
    updated = user_crud.update_user(session, user_id, user_in.status)
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={user_id} not found",
        )
    return updated


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: int,
    session: Session = Depends(db.get_db),
) -> None:
    """
    Delete a user by its ID.

    Raises 404 if not found. Returns 204 No Content on success.
    """
    success = user_crud.delete_user(session, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id={user_id} not found",
        )
    return None
