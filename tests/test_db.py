"""Tests for the db module."""
from src.app import db


def test_get_db() -> None:
    """It returns a database connection."""
    assert db.database is not None
