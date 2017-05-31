"""Test deque"""
import pytest

PARAMETERS_FOR_APPEND_LEFT_AND_APPEND = [
    ('abcde', 5),
    ([], 0),
    ([1, 2, 3, 4, 5, 6, 8], 7),
    ('c.r.e.a.m.', 10),
    (['eins', 'zwei', 'drei'], 3)
]

PARAMETERS_FOR_PEEK = [
    ('abcde', 'e'),
    ([], None),
    ([1, 2, 3, 4, 5, 6, 8], 8),
    ('c.r.e.a.m.', '.'),
    (['eins', 'zwei', 'drei'], 'drei')
]

PARAMETERS_FOR_PEEK_WITH_APPEND_LEFT = [
    ('abcde', 'a'),
    ([], None),
    ([1, 2, 3, 4, 5, 6, 8], 1),
    ('c.r.e.a.m.', 'c'),
    (['a', 'b', 'c'], 'a')
]

PARAMETERS_FOR_PEEK_LEFT = [
    ('abcde', 'a'),
    ([], None),
    ([1, 2, 3, 4, 5, 6, 8], 1),
    ('c.r.e.a.m.', 'c'),
    (['a', 'b', 'c'], 'a')
]

PARAMETERS_FOR_POP_AND_POPLEFT = [
    (2, 8),
    (4, 6),
    (6, 4),
    (10, 0),
    (5, 5),
    (7, 3),
    (8, 2),
    (9, 1)
]


@pytest.fixture
def empty_deque():
    """This fixture returns an empty deque fixture"""
    from deque import Deque
    return Deque()


@pytest.fixture
def deque_with_values():
    """This fixture returns a deque with values"""
    from deque import Deque
    test_deque = Deque()

    for value in range(10):
        test_deque.appendleft(value + 1)
    return test_deque


def test_init(empty_deque):
    """
    Asserts that the initializer returns a deque with the head and tail equal to None
    """
    assert empty_deque.head == None and empty_deque.tail == None


def test_size_of_empty_deque(empty_deque):
    """
    Asserts that the initializer returns a deque with a size of 0
    """
    assert empty_deque.size() == 0


def test_popleft_empty_deque_error_raised(empty_deque):
    """Assertion: Raises appropriate exception when trying to popleft from an empty deque."""

    with pytest.raises(IndexError):
        empty_deque.popleft()


def test_pop_empty_deque_error_raised(empty_deque):
    """Assertion: Raises appropriate exception when trying to pop from an empty deque."""

    with pytest.raises(IndexError):
        empty_deque.pop()


@pytest.mark.parametrize('number_of_calls_to_pop, result', PARAMETERS_FOR_POP_AND_POPLEFT)
def test_size(number_of_calls_to_pop, result, deque_with_values):
    """
    Asserts the after x number of calls to the pop function, the deque will be length of size - x
    """
    for i in range(number_of_calls_to_pop):
        deque_with_values.pop()
    assert deque_with_values.size() == result


@pytest.mark.parametrize('number_of_calls_to_pop, result', PARAMETERS_FOR_POP_AND_POPLEFT)
def test_popleft(number_of_calls_to_pop, result, deque_with_values):
    """
    Asserts the after x number of calls to the popleft function, the deque will be length of size - x
    """
    for i in range(number_of_calls_to_pop):
        deque_with_values.pop()
    assert deque_with_values.size() == result


@pytest.mark.parametrize('number_of_calls_to_pop, result', PARAMETERS_FOR_POP_AND_POPLEFT)
def test_pop(number_of_calls_to_pop, result, deque_with_values):
    """
    Asserts the after x number of calls to the pop function, the deque will be length of size - x
    """
    for i in range(number_of_calls_to_pop):
        deque_with_values.pop()
    assert deque_with_values.size() == result


@pytest.mark.parametrize('values, result', PARAMETERS_FOR_PEEK_WITH_APPEND_LEFT)
def test_peek_with_appendleft(values, result, empty_deque):
    """Asserts that the last item to be appended is the return value of the call to peek function"""
    for value in values:
        empty_deque.appendleft(value)
    assert empty_deque.peek() == result


@pytest.mark.parametrize('values, result', PARAMETERS_FOR_PEEK_LEFT)
def test_peekleft(values, result, empty_deque):
    """Asserts the last item item to be appended is the return value of the call to peekleft function"""
    for value in values:
        empty_deque.append(value)
        assert empty_deque.peekleft() == result


@pytest.mark.parametrize('values, result', PARAMETERS_FOR_PEEK)
def test_peek(values, result, empty_deque):
    """Asserts that the last item to be appended is the return value of the call to peek function"""
    for value in values:
        empty_deque.append(value)
    assert empty_deque.peek() == result


@pytest.mark.parametrize('values, result', PARAMETERS_FOR_APPEND_LEFT_AND_APPEND)
def test_append_left(values, result, empty_deque):
    """Asserts that the length of the deque is equal to the number of values passed in"""
    for value in values:
        empty_deque.appendleft(value)

    assert empty_deque.size() == result


@pytest.mark.parametrize('values, result', PARAMETERS_FOR_APPEND_LEFT_AND_APPEND)
def test_append(values, result, empty_deque):
    """Asserts that the length of the deque is equal to the number of values passed in"""
    for value in values:
        empty_deque.append(value)

    assert empty_deque.size() == result

