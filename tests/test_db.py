"""Tests for the db module."""
from unittest import mock
from unittest.mock import Mock

with mock.patch("databases.Database") as _mock_db:
    with mock.patch("pydantic.BaseSettings") as mock_settings:
        p = mock.PropertyMock(return_value="sqlite://")
        type(mock_settings).db_url = p
        from src.app import db


def test_get_db(mock_db: Mock) -> None:
    """It returns a database connection."""
    assert db.database == mock_db
