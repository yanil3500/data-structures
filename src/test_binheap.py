"""Test the binary heap ADT."""
import pytest
from binheap import BinaryHeap


@pytest.fixture
def empty_bin_heap():
    from binheap import BinaryHeap
    return BinaryHeap()


@pytest.fixture
def bin_heap_with_values():
    from binheap import BinaryHeap
    return BinaryHeap([4, 9, 3, 18, 1, 6])


def test_push_empty_bin_heap(empty_bin_heap, value_to_push):
    from binheap import BinaryHeap
    empty_bin_heap.push(value_to_push)
    assert empty_bin_heap.items[0] == value_to_push


PUSH_BIN_HEAP_WITH_VALUES_TABLE = [
    (bin_heap_with_values)
]


def test_push_bin_heap_with_values(bin_heap_with_values, value_to_push):
    from binheap import BinaryHeap