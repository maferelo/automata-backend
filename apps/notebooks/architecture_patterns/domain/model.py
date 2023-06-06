"""Domain model for the allocation service.""" ""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Set


class OutOfStock(Exception):
    """Exception raised when there is no stock available for an order line."""


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    """Allocate an order line to a batch."""
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration as exc:
        raise OutOfStock(f"Out of stock for sku {line.sku}") from exc


@dataclass(frozen=True)
class OrderLine:
    """An order line in an order."""

    orderid: str
    sku: str
    qty: int


class Batch:
    """A batch of stock for a particular product."""

    def __init__(self, ref: str, sku: str, qty: int, eta: date | None):
        """Create a new batch of stock."""
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[OrderLine]

    def __repr__(self) -> str:
        """Return a string representation of a batch."""
        return f"<Batch {self.reference}>"

    def __eq__(self, other: object) -> bool:
        """Compare two batches for equality."""
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        """Return a hash of a batch."""
        return hash(self.reference)

    def __gt__(self, other):
        """Compare two batches for sorting."""
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        """Allocate an order line to this batch."""
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        """Deallocate an order line from this batch."""
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        """Return the total quantity allocated to order lines."""
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        """Return the quantity of stock available for allocation."""
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        """Return True if there is stock available for an order line."""
        return self.sku == line.sku and self.available_quantity >= line.qty
