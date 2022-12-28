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
