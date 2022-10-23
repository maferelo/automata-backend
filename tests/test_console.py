import click.testing
import pytest
import requests

from app import console


@pytest.fixture(name="runner")
def runner_ficture():
    return click.testing.CliRunner()


@pytest.fixture(name="mock_wikipedia_random_page")
def mock_wikipedia_random_page_fixture(mocker):
    return mocker.patch("app.wikipedia.random_page")


def test_main_fails_on_request_error(runner, _mock_requests_get):
    _mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_invokes_requests_get(runner, _mock_requests_get):
    runner.invoke(console.main)
    assert _mock_requests_get.called


def test_main_prints_message_on_request_error(runner, _mock_requests_get):
    _mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_prints_title(runner, _mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_uses_en_wikipedia_org(runner, _mock_requests_get):
    runner.invoke(console.main)
    args, _ = _mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_succeeds(runner, _mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")
