"""Tests for the utils module."""
import pytest

from src.app import utils

TEST_FILE_HASH = "7a7f969187878d2fc73b1b97c4cd38467e737089dd2c4186d24ed3b20133f9ec"
TEST_FILE_TO_HASH_PATH = "tests/data/test.txt"


def test_get_file_hash() -> None:
    """It returns the SHA256 hash of a file."""
    assert utils.get_file_hash(TEST_FILE_TO_HASH_PATH) == TEST_FILE_HASH


def test_save_file_hash() -> None:
    """It saves the SHA256 hash of a file."""
    utils.save_file_hash(TEST_FILE_TO_HASH_PATH)
    with open(f"{TEST_FILE_TO_HASH_PATH}.sha256", encoding="utf-8") as file:
        file_hash = file.read()
        assert file_hash == TEST_FILE_HASH


def test_validate_file_hash() -> None:
    """It validates the SHA256 hash of a file."""
    print("Saving hash...test_validate_file_hash")
    utils.save_file_hash(TEST_FILE_TO_HASH_PATH)
    assert utils.validate_file_hash(TEST_FILE_TO_HASH_PATH) is True


def test_validate_file_hash_fails() -> None:
    """It fails to validate the SHA256 hash of a file that does not exist."""
    with pytest.raises(FileNotFoundError):
        utils.validate_file_hash("tests/data/does-not-exist.txt")
