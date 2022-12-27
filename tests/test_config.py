"""Tests for the config module."""
from unittest import mock

with mock.patch("pydantic.BaseSettings") as mock_method:
    p = mock.PropertyMock(return_value="sqlite://")
    type(mock_method).db_url = p
    from src.app import config


def test_settings() -> None:
    """It returns the application settings."""
    assert mock_method == config.settings
