"""Test the model module."""
from datetime import date

from model import Batch
from model import OrderLine


def test_batch_repr() -> None:
    """Test the batch representation."""
    batch = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    assert repr(batch) == "<Batch batch-001>"


def test_batch_eq() -> None:
    """Test the batch equality."""
    batch1 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    batch2 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    assert batch1 == batch2


def test_batch_eq_bad_type() -> None:
    """Test the batch equality with a bad type."""
    batch1 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    assert batch1 != "batch-001"


def test_batch_hash() -> None:
    """Test the batch hash."""
    batch1 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    batch2 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    assert hash(batch1) == hash(batch2)


def test_batch_qty() -> None:
    """Test the batch quantity."""
    batch1 = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    batch2 = Batch("batch-001", "SMALL-TABLE", 100, eta=date.today())
    assert batch1 < batch2


def test_batch_allocation() -> None:
    """Test the batch allocation."""
    batch = Batch("batch-001", "SMALL-TABLE", 100, eta=None)
    line = OrderLine("order-123", "SMALL-TABLE", 110)
    assert batch.allocate(line) is None
