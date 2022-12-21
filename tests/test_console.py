"""Test cases for the console module."""
from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from src.app import console


@pytest.fixture
def _runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def _mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Fixture for mocking wikipedia.random_page."""
    return mocker.patch("src.app.wikipedia.random_page")


def test_main_succeeds(_runner: CliRunner, _mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = _runner.invoke(console.main)
    assert result.exit_code == 0


@pytest.mark.e2e
def test_main_succeeds_in_production_env(_runner: CliRunner) -> None:
    """It exits with a status code of zero (end-to-end)."""
    result = _runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(_runner: CliRunner, _mock_requests_get: Mock) -> None:
    """It prints the title of the Wikipedia page."""
    result = _runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(
    _runner: CliRunner, _mock_requests_get: Mock
) -> None:
    """It invokes requests.get."""
    _runner.invoke(console.main)
    assert _mock_requests_get.called


def test_main_uses_en_wikipedia_org(
    _runner: CliRunner, _mock_requests_get: Mock
) -> None:
    """It uses the English Wikipedia by default."""
    _runner.invoke(console.main)
    args, _ = _mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_uses_specified_language(
    _runner: CliRunner, _mock_wikipedia_random_page: Mock
) -> None:
    """It uses the specified language edition of Wikipedia."""
    _runner.invoke(console.main, ["--language=pl"])
    _mock_wikipedia_random_page.assert_called_with(language="pl")


def test_main_fails_on_request_error(
    _runner: CliRunner, _mock_requests_get: Mock
) -> None:
    """It exits with a non-zero status code if the request fails."""
    _mock_requests_get.side_effect = Exception("Boom")
    result = _runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    _runner: CliRunner, _mock_requests_get: Mock
) -> None:
    """It prints an error message if the request fails."""
    _mock_requests_get.side_effect = requests.RequestException
    result = _runner.invoke(console.main)
    assert "Error" in result.output
