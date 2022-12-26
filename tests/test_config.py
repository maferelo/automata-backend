"""Tests for the config module."""
from pydantic import BaseSettings

from src.app import config


def test_settings() -> None:
    """It returns the application settings."""
    assert isinstance(config.settings, BaseSettings)
