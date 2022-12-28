"""Utility functions for the app."""
import hashlib


def get_file_hash(file_path: str) -> str:
    """Get the SHA256 hash of a file."""
    with open(file_path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


def save_file_hash(file_path: str) -> None:
    """Save the SHA256 hash of a file."""
    file_hash = get_file_hash(file_path)
    with open(f"{file_path}.sha256", "w", encoding="utf-8") as file:
        file.write(file_hash)


def validate_file_hash(file_path: str) -> bool:
    """Validate the SHA256 hash of a file."""
    try:
        with open(f"{file_path}.sha256", encoding="utf-8") as file:
            expected_hash = file.read()
    except FileNotFoundError:
        expected_hash = None
        save_file_hash(file_path)
    return expected_hash == get_file_hash(file_path)
