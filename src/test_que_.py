"""Test que_.py"""

import pytest

ENQUEUE_TABLE = [
    ([10, 50, 100, 5000], 10000, 5),
    ([1, 2, 3], 99, 4),
    (['one', 'two', 'three', 'four'], 88822, 5),
    ([], 'one', 1)
]

DEQUEUE_TABLE = [
    (1),
    ('two'),
    ([1, 2, 3, 4, 5])
]


@pytest.fixture
def empty_que():
    """Return empty queue fixture."""
    from que_ import Queue
    return Queue()

@pytest.fixture
def que_with_values():
    """Return queue with values fixture."""
    from que_ import Queue
    q = Queue()

    for i in range(10):
        q.enqueue(i + 1)

    return q

def test_init(empty_que):
    """Asssert if init function is valid."""
    assert empty_que._length == 0 and empty_que._front is None and empty_que._rear is None


@pytest.mark.parametrize('list_of_values, value_to_enqueue, new_length', ENQUEUE_TABLE)
def test_enqueue(list_of_values, value_to_enqueue, new_length, empty_que):
    """Assert if enqueue passes tests."""
    from que_ import Queue
    from que_ import Node
    for i in range(len(list_of_values)):
        empty_que.enqueue(list_of_values[i])
    empty_que.enqueue(value_to_enqueue)

    assert empty_que._rear.value == value_to_enqueue and empty_que._length == new_length


def test_dequeue(que_with_values):
    """
    Assert if dequeue is valid with queue with values.
    que_with_values is (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """
    from que_ import Queue
    from que_ import Node
    dq_value = que_with_values.dequeue()
    assert  dq_value == 1 and que_with_values._length == 9 and que_with_values._front.value == 2


def test_dequeue_empty_queue(empty_que):
    """Assert if dequeue raises appropriate exception when trying to dequeue an empty queue."""
    from que_ import Queue
    from que_ import Node
    with pytest.raises(IndexError):
        empty_que.dequeue()


def test_peek_queue(que_with_values):
    """
    Assert if peek value is valid.
    que_with_values is (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """
    from que_ import Queue
    from que_ import Node
    assert que_with_values.peek() == 1


def test_peek_empty_queue(empty_que):
    """
    Assert if peek returns None if peek on empty queue.
    """
    from que_ import Queue
    from que_ import Node
    assert empty_que.peek() is None


def test_size(que_with_values):
    """
    Assert queue size is valid.
    que_with_values is (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """
    assert que_with_values.size() == 10 and que_with_values._length == 10


def test_size_empty_queue(empty_que):
    """
    Assert size return 0 for empty queue. 
    """
    assert empty_que.size() == 0 and empty_que._length == 0