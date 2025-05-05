import json
from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session

from ..models import PartnerTable


def list_partners(db: Session) -> List[Dict[str, Any]]:
    """
    Retrieve all partners from the database.

    Args:
        db: database session

    Returns:
        A list of dicts, each containing 'id' and the parsed 'data'.
    """
    rows = db.query(PartnerTable).all()
    return [{"id": row.id, "data": json.loads(row.data)} for row in rows]


def create_partner(
    db: Session,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Create and persist a new partner.

    Args:
        db: database session
        data: arbitrary JSON-serializable payload

    Returns:
        A dict with 'id' and the original 'data'.
    """
    row = PartnerTable(data=json.dumps(data))
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "data": data}


def get_partner(
    db: Session,
    partner_id: int,
) -> Optional[Dict[str, Any]]:
    """
    Retrieve a single partner by ID.

    Args:
        db: database session
        partner_id: primary key of the partner

    Returns:
        A dict with 'id' and parsed 'data', or None if not found.
    """
    row = db.query(PartnerTable).filter(PartnerTable.id == partner_id).first()
    if not row:
        return None
    return {"id": row.id, "data": json.loads(row.data)}


def update_partner(
    db: Session,
    partner_id: int,
    data: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    """
    Replace an existing partner’s payload.

    Args:
        db: database session
        partner_id: primary key of the partner
        data: new JSON-serializable payload

    Returns:
        A dict with updated 'id' and 'data', or None if not found.
    """
    row = db.query(PartnerTable).filter(PartnerTable.id == partner_id).first()
    if not row:
        return None

    row.data = json.dumps(data)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "data": data}


def delete_partner(db: Session, partner_id: int) -> bool:
    """
    Delete a partner by ID.

    Args:
        db: database session
        partner_id: primary key of the partner

    Returns:
        True if deleted, False if no such partner existed.
    """
    row = db.query(PartnerTable).filter(PartnerTable.id == partner_id).first()
    if not row:
        return False

    db.delete(row)
    db.commit()
    return True
