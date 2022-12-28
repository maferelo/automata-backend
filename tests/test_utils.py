"""Tests for the utils module."""
import pytest

from src.app import utils


def test_get_file_hash() -> None:
    """It returns the SHA256 hash of a file."""
    assert utils.get_file_hash("tests/data/test.txt") == (
        "7a7f969187878d2fc73b1b97c4cd38467e737089dd2c4186d24ed3b20133f9ec"
    )


def test_save_file_hash() -> None:
    """It saves the SHA256 hash of a file."""
    utils.save_file_hash("tests/data/test.txt")
    with open("tests/data/test.txt.sha256", encoding="utf-8") as file:
        assert file.read() == (
            "7a7f969187878d2fc73b1b97c4cd38467e737089dd2c4186d24ed3b20133f9ec"
        )


def test_validate_file_hash() -> None:
    """It validates the SHA256 hash of a file."""
    utils.save_file_hash("tests/data/test.txt")
    assert utils.validate_file_hash("tests/data/test.txt") is True


def test_validate_file_hash_fails() -> None:
    """It fails to validate the SHA256 hash of a file that does not exist."""
    with pytest.raises(FileNotFoundError):
        utils.validate_file_hash("tests/data/does-not-exist.txt")
