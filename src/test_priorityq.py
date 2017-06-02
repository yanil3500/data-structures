""""Tests for our priority queue"""
import pytest

# insert(value): inserts a value into the queue. Takes an optional argument for that value’s priority, set by default to whatever your lowest priority is (i.e. 0, -99, whatever).

# pop(): removes the most important item from the queue and returns its value.

# peek(): returns the most important item without removing it from the queue

# I'm going to assume that the highest priority level is 1 
# Assume that the first item in the tuple is the value to be inserted; Assume that the second item in the tuple is that value's priority level
PARAMETERS_FOR_INSERT_WITH_PRIORITY_LEVELS = [
    ([(5, 1), (99, 56), (6, 4), (8, 10), (7, 6), (9, 10), (3, 2)], 7),
    ([(3, 4), (2, 1), (5, 8), (3, 6)], 4),
    ([(8, 9)], 1),
    ([(300, 2), (300, 5)])
]

PARAMETERS_FOR_POP = [
    ([(5, 1), (98, 1), (6, 3), (8, 10), (7, 10), (9, 11), (3, 1)], 3, 3),
    ([(3, 4), (2, 1), (5, 4), (3, 8)], 2, 3),
    ([(7, 9), (1000, 9)], 1, 7),
    ([(300, 2), (300, 5), (50, 2)], 1, 300),
    ([(500, 1), (6, 2), (45, 9)], 2, 6),
    ([(1,), (8,), (67,)], 2, 8)
]


@pytest.fixture
def empty_priorityq():
    """
    This fixture will return an priority q
    """
    from priorityq import PriorityQ
    return PriorityQ()


@pytest.mark.parametrize('values, expected_priorityq_size', PARAMETERS_FOR_INSERT_WITH_PRIORITY_LEVELS)
def test_insert_with_priority_levels(values, expected_priorityq_size, empty_priorityq):
    """
    This function asserts that the size of the priorityq will be proportional to
    the number of values insert into the priorityq
    """
    for value_and_priority in values:
        empty_priorityq.insert(value_and_priority[0], priority=value_and_priority[1])
    assert empty_priorityq.size == expected_priorityq_size


@pytest.mark.parametrize('values, number_calls_to_pop_function, expected_result', PARAMETERS_FOR_POP)
def test_pop(values, number_calls_to_pop_function, expected_result, empty_priorityq):
    """
    This function asserts that the priorityq will return the value with the highest level of importance; If two or more values have the same priority level, then the values are removed according to their order in the queue. (The order in which they were inserted)
    """
    for value_and_priority in values:
        if len(value_and_priority) == 1:
            empty_priorityq.insert(value_and_priority[0])
        else:
            empty_priorityq.insert(value_and_priority[0], priority=empty_priorityq.insert(value_and_priority[1]))
    for val in range(0, number_calls_to_pop_function):
        last_value_popped = empty_priorityq.pop()
    assert last_value_popped == expected_result





