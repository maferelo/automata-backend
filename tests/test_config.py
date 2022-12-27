"""Tests for the config module."""
from unittest.mock import Mock

from src.app import config


def test_settings(mock_settings: Mock) -> None:
    """It returns the application settings."""
    assert mock_settings == config.settings
