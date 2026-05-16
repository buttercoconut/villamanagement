"""Utility functions – currently only fee calculation.

The calculation logic is intentionally simple: a resident's total
unpaid fees are summed.  In a real system you would probably have
more sophisticated rules (e.g. discounts, late fees, tax, etc.).
"""

from datetime import date
from typing import Iterable

from sqlalchemy.orm import Session

from models import Fee, Resident


def calculate_total_due(db: Session, resident_id: int, as_of: date | None = None) -> float:
    """Return the sum of unpaid fees for *resident_id*.

    Parameters
    ----------
    db:
        SQLAlchemy session.
    resident_id:
        ID of the resident.
    as_of:
        Optional date to consider fees due up to this date.
    """
    query = db.query(Fee).filter(Fee.resident_id == resident_id, Fee.paid == False)
    if as_of:
        query = query.filter(Fee.due_date <= as_of)
    return float(sum(f.amount for f in query.all()))
