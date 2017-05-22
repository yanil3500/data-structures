
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
    (10, 10)
]

MOCK_LINKED_LIST = linked_list.LinkedList()


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
    MOCK_LINKED_LIST.push(val)
    temp_node = (MOCK_LINKED_LIST.pop())
    assert isinstance(temp_node, linked_list.Node)
    assert  temp_node == result



