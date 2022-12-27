"""Tests for the db module."""
from unittest import mock
from unittest.mock import Mock

with mock.patch("databases.Database") as mock_method:
    from src.app import db


def test_get_db(mock_db: Mock) -> None:
    """It returns a database connection."""
    assert db.database == mock_db
