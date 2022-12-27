"""Tests for the db module."""
from unittest.mock import Mock

from src.app import db


def test_get_db(mock_db: Mock) -> None:
    """It returns a database connection."""
    assert db.database == mock_db
