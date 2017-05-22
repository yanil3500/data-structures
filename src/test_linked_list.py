
"""
Tests for counting duplicates
"""
import pytest
import linked_list
PARAMETERS_LIST_FOR_PUSH = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (100, 5)
]

PARAMETERS_LIST_FOR_POP = [
    (1, 1),
    (999, 999),
    (10, 10),
    (55, 55)
]

PARAMETERS_LIST_FOR_SIZE = [
    ('A', 1),
    ('B', 2),
    (5, 3),
    (5, 4),
    (1000, 5)
]

PARAMETERS_LIST_FOR_SEARCH = [
    (1, linked_list.Node),
    (2, linked_list.Node),
    (3, linked_list.Node),
    (4, linked_list.Node),
    (5, None),
    (7, None)
]

PARAMETERS_LIST_FOR_REMOVE = [
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (1000, False),
    (7, False)
]

MOCK_LINKED_LIST = linked_list.LinkedList()


def helper_teardown(an_object):
    """
    reset the linked list
    """
    an_object.head = None
    an_object.length = 0


@pytest.mark.parametrize('val, result', PARAMETERS_LIST_FOR_PUSH)
def test_push(val, result):
    """
    test push function
    """
    MOCK_LINKED_LIST.push(val)
    assert MOCK_LINKED_LIST.size() == result


@pytest.mark.parametrize('val, result', PARAMETERS_LIST_FOR_POP)
def test_pop(val, result):
    """
    test pop function
    """
    helper_teardown(MOCK_LINKED_LIST)
    MOCK_LINKED_LIST.push(val)
    temp_node = (MOCK_LINKED_LIST.pop())
    assert temp_node.val == result


@pytest.mark.parametrize('val, result', PARAMETERS_LIST_FOR_SIZE)
def test_size(val, result):
    """
    test for size function
    """
    MOCK_LINKED_LIST.push(val)
    assert MOCK_LINKED_LIST.size() == result


@pytest.mark.parametrize('val, result', PARAMETERS_LIST_FOR_SEARCH)
def test_search(val, result):
    """
    test for search function
    """
    for number in range(0, 5):
        MOCK_LINKED_LIST.push(number)

    result = MOCK_LINKED_LIST.search(val)
    assert MOCK_LINKED_LIST.search(val) == result


@pytest.mark.parametrize('value, result', PARAMETERS_LIST_FOR_REMOVE)
def test_remove(value, result):
    """
    test for remove method
    """
    helper_teardown(MOCK_LINKED_LIST)
    for number in range(0, 5):
        print('The number before being push onto list: {}'.format(number))
        MOCK_LINKED_LIST.push(number)
    node_from_list = MOCK_LINKED_LIST.search(value)
    assert MOCK_LINKED_LIST.remove(node_from_list) == result
