"""Test the binary heap ADT."""
import pytest


VALUES_TO_PUSH_TO_EMPTY_BINHEAP = [
    (1),
    (9),
    (-1900),
    (1.288999)
]


VALUES_TO_PUSH_TO_BINHEAP_WITH_VALUES = [
    (0, [0, 3, 1, 18, 9, 6, 4]),
    (99999, [1, 3, 4, 18, 9, 6, 99999]),
    (9, [1, 3, 4, 18, 9, 6, 9])
]


INIT_VALUES_TABLE = [
    ([1, 2, 3, 4], 4),
    ([], 0)
]

SWAP_TABLE = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 1, 2, 1),
    ([99, 1, 88, 2, 77], 2, 3, 2, 88)
]

LEFT_CHILD_TABLE = [
    ([5, 2, 1, 8, 9 ,18], 0, 1),
    ([4, 9, 3, 18, 1, 6], 2, 5)
]

RIGHT_CHILD_TABLE = [
    ([5, 2, 1, 8, 9 ,18], 0, 2),
    ([4, 9, 3, 18, 1, 6], 2, 6)
]

PARENT_INDEX_TABLE = [
    ([5, 2, 1, 8, 9, 18], 3, 1),
    ([4, 9, 3, 18, 1, 6], 4, 1)
]


@pytest.fixture
def empty_bin_heap():
    from binheap import BinaryHeap
    bin_heap = BinaryHeap()
    return bin_heap


@pytest.fixture
def bin_heap_with_values():
    from binheap import BinaryHeap
    return BinaryHeap([4, 9, 3, 18, 1, 6])


def test_init_no_params(empty_bin_heap):
    from binheap import BinaryHeap
    assert empty_bin_heap.length == 0


@pytest.mark.parametrize('list, length', INIT_VALUES_TABLE)
def test_init_with_values(list, length):
    from binheap import BinaryHeap
    assert BinaryHeap(list).length == length


@pytest.mark.parametrize('value', VALUES_TO_PUSH_TO_EMPTY_BINHEAP)
def test_push_empty_bin_heap(empty_bin_heap, value):
    from binheap import BinaryHeap
    empty_bin_heap.push(value)
    assert empty_bin_heap.items[0] == value


@pytest.mark.parametrize('value, list_after_push', VALUES_TO_PUSH_TO_BINHEAP_WITH_VALUES)
def test_push_bin_heap_with_values(value, list_after_push, bin_heap_with_values):
    from binheap import BinaryHeap
    bin_heap = bin_heap_with_values
    bin_heap.push(value)
    assert bin_heap.items == list_after_push


@pytest.mark.parametrize('list, first_index, second_index, new_first_value, new_second_value', SWAP_TABLE)
def test_swap(list, first_index, second_index, new_first_value, new_second_value):
    """Assert that swap function passes."""
    from binheap import BinaryHeap
    bh = BinaryHeap()
    bh.items = list
    bh.swap(first_index, second_index)
    assert bh.items[first_index] == new_first_value and bh.items[second_index] == new_second_value


@pytest.mark.parametrize('list, parent_index, left_index', LEFT_CHILD_TABLE)
def test_left_child_index(list, parent_index, left_index):
    """Assert that we get correct left child index."""
    from binheap import BinaryHeap
    bh = BinaryHeap(list)
    assert bh.left_child_index(parent_index) == left_index


@pytest.mark.parametrize('list, parent_index, right_index', RIGHT_CHILD_TABLE)
def test_right_child_index(list, parent_index, right_index):
    """Assert that we get correct right child index."""
    from binheap import BinaryHeap
    bh = BinaryHeap(list)
    assert bh.right_child_index(parent_index) == right_index


@pytest.mark.parametrize('list, child_index, parent_index', PARENT_INDEX_TABLE)
def test_parent_index(list, child_index, parent_index):
    """Assert that we get correct parent index."""
    from binheap import BinaryHeap
    bh = BinaryHeap(list)
    assert bh.parent_index(child_index) == parent_index


