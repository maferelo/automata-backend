"""Package-wide test fixtures."""
from unittest.mock import Mock

import pytest
from _pytest.config import Config
from pytest_mock import MockFixture

TO_HASH_FILE_PATH = "tests/data/test.txt"


def pytest_configure(config: Config) -> None:
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture(name="mock_db")
def mock_db(mocker: MockFixture) -> Mock:
    """Fixture for mocking settings."""
    return mocker.patch("src.app.db.database")


@pytest.fixture(name="_mock_requests_get")
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


@pytest.fixture(name="mock_file_open")
def mock_file_open(mocker: MockFixture) -> Mock:
    """Fixture for mocking open."""
    mocked_hash_data = mocker.mock_open(read_data="hash")
    return mocker.patch("builtins.open", mocked_hash_data)


@pytest.fixture(name="mock_get_file_hash")
def mock_get_file_hash(mocker: MockFixture) -> Mock:
    """Fixture for mocking utils.get_file_hash."""
    return mocker.patch("src.app.utils.get_file_hash", return_value="hash")
