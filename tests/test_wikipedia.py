"""Test cases for the wikipedia module."""
from unittest.mock import Mock

import click
import pytest

from app import wikipedia


def test_random_page_uses_given_language(_mock_requests_get: Mock) -> None:
    """It selects the specified Wikipedia language edition."""
    wikipedia.random_page(language="de")
    args, _ = _mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(_mock_requests_get: Mock) -> None:
    """It returns an object of type Page."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(_mock_requests_get: Mock) -> None:
    """It raises `ClickException` when validation fails."""
    _mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()
