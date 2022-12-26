"""Tests for the utils module."""
import pytest

from src.app import utils


def test_get_file_hash() -> None:
    """It returns the SHA256 hash of a file."""
    assert utils.get_file_hash("tests/data/test.txt") == (
        "df5f5e4c517baba6abb156b2b549cecc3a0e0cc6148f66814d956d41a1675820"
    )


def test_save_file_hash() -> None:
    """It saves the SHA256 hash of a file."""
    utils.save_file_hash("tests/data/test.txt")
    with open("tests/data/test.txt.sha256", encoding="utf-8") as file:
        assert file.read() == (
            "df5f5e4c517baba6abb156b2b549cecc3a0e0cc6148f66814d956d41a1675820"
        )


def test_validate_file_hash() -> None:
    """It validates the SHA256 hash of a file."""
    assert utils.validate_file_hash("tests/data/test.txt") is True


def test_validate_file_hash_fails() -> None:
    """It fails to validate the SHA256 hash of a path that does not exist."""
    with pytest.raises(FileNotFoundError):
        assert utils.validate_file_hash("tests/data/does-not-exist.txt") is False
