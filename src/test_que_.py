"""Test que_.py"""

import pytest

ENQUEUE_TABLE = [
    ([10, 50, 100, 5000], 10000, 5),
    ([1, 2, 3], 99, 4),
    (['one', 'two', 'three', 'four'], 88822, 5),
    ([], 'one', 1)
]

@pytest.fixture
def empty_que():
    """The empty_que funciton returns an empty queue as a fixture."""
    from que_ import Queue
    return Queue()

@pytest.fixture
def que_with_values():
    """The que_with_values returns a queue with values as fixture."""
    from que_ import Queue
    q = Queue()

    for i in range(10):
        q.enqueue(i + 1)

    return q

@pytest.fixture
def que_with_one_value():
    """The que_with_one_value returns a queue containing one value as a fixture."""
    from que_ import Queue
    q = Queue()
    q.enqueue(1)
    return q

def test_init(empty_que):
    """Asserts that the init function is valid."""
    assert empty_que._length == 0 and empty_que._front is None and empty_que._rear is None


@pytest.mark.parametrize('list_of_values, value_to_enqueue, new_length', ENQUEUE_TABLE)
def test_enqueue(list_of_values, value_to_enqueue, new_length, empty_que):
    """Asserts that the enqueue method is in working order when adding multiple item to a queue.."""
    from que_ import Queue
    from que_ import Node
    for i in range(len(list_of_values)):
        empty_que.enqueue(list_of_values[i])
    empty_que.enqueue(value_to_enqueue)

    assert empty_que._rear.value == value_to_enqueue and empty_que._length == new_length


def test_dequeue(que_with_values):
    """
    Asserts that the dequeue method is in working order when called on a queue that contains more than one item.
    que_with_values is (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    """
    from que_ import Queue
    from que_ import Node
    dq_value = que_with_values.dequeue()
    assert  dq_value == 1 and que_with_values._length == 9 and que_with_values._front.value == 2


def test_dequeue_one_value(que_with_one_value):
    """
    Asserts that the dequeue method is in working order when called on a queue that contains one item.
    que_with_one_value is (1)
    """
    from que_ import Queue
    from que_ import Node
    dq_value = que_with_one_value.dequeue()
    assert  dq_value == 1 and que_with_one_value._length == 0 and que_with_one_value._front is None


def test_dequeue_empty_queue(empty_que):
    """Asserts that an appropriate exception is raised when trying to dequeue an item from an empty queue."""
    from que_ import Queue
    from que_ import Node
    with pytest.raises(IndexError):
        empty_que.dequeue()


def test_peek_queue(que_with_values):
    """
    Asserts that peek returns the correct value; That returns the value at the front of the queue.
    """
    from que_ import Queue
    from que_ import Node
    assert que_with_values.peek() == 1


def test_peek_empty_queue(empty_que):
    """
    Asserts that peek returns None if peek is called on an empty queue.
    """
    from que_ import Queue
    from que_ import Node
    assert empty_que.peek() is None


def test_size(que_with_values):
    """
    Asserts that queue size is valid when given a queue containing 10 elements.
    """
    assert que_with_values.size() == 10 and que_with_values._length == 10


def test_size_empty_queue(empty_que):
    """
    Asserts that size method returns 0 for an empty queue.
    """
    assert empty_que.size() == 0 and empty_que._length == 0