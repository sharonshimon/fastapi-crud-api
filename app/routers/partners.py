from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud.partner_crud import (
    create_partner as crud_create_partner,
    get_partner as crud_get_partner,
    list_partners as crud_list_partners,
    update_partner as crud_update_partner,
    delete_partner as crud_delete_partner,
)
from ..db import get_db
from ..models import Partner

router = APIRouter(
    prefix="/partners",
    tags=["partners"],
)


@router.get(
    "/",
    response_model=List[Partner],
    status_code=status.HTTP_200_OK,
)
def get_all_partners(
    session: Session = Depends(get_db),
) -> List[Partner]:
    """
    List all partners.

    Returns an empty list if no partners exist.
    """
    partners = crud_list_partners(session)
    return partners


@router.post(
    "/",
    response_model=Partner,
    status_code=status.HTTP_201_CREATED,
)
def create_new_partner(
    partner_in: Partner,
    session: Session = Depends(get_db),
) -> Partner:
    """
    Create a new partner with arbitrary JSON payload.

    Expects:
        {
            "data": { ... }
        }
    """
    return crud_create_partner(session, partner_in.data)


@router.get(
    "/{partner_id}",
    response_model=Partner,
)
def get_partner_by_id(
    partner_id: int,
    session: Session = Depends(get_db),
) -> Partner:
    """
    Retrieve a partner by its ID.

    Raises 404 if not found.
    """
    partner = crud_get_partner(session, partner_id)
    if partner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Partner with id={partner_id} not found",
        )
    return partner


@router.put(
    "/{partner_id}",
    response_model=Partner,
)
def replace_partner_by_id(
    partner_id: int,
    partner_in: Partner,
    session: Session = Depends(get_db),
) -> Partner:
    """
    Replace an existing partner’s payload.

    Expects:
        {
            "data": { ... }
        }
    Raises 404 if not found.
    """
    updated = crud_update_partner(session, partner_id, partner_in.data)
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Partner with id={partner_id} not found",
        )
    return updated


@router.delete(
    "/{partner_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_partner_by_id(
    partner_id: int,
    session: Session = Depends(get_db),
) -> None:
    """
    Delete a partner by its ID.

    Raises 404 if not found.
    """
    deleted = crud_delete_partner(session, partner_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Partner with id={partner_id} not found",
        )
    # FastAPI will return a 204 No Content with no body
    return None