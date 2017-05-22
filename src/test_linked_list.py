
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
    (linked_list.Node),
    (linked_list.Node),
    (linked_list.Node),
    (linked_list.Node),
    (linked_list.Node),
]

MOCK_LINKED_LIST = linked_list.Singly_Linked_List()


@pytest.mark.parametrize('val, result', PARAMETERS_LIST_FOR_PUSH)
def test_push(val, result):
    """
    test push function
    """
    MOCK_LINKED_LIST.push(val)
    assert MOCK_LINKED_LIST.size() == result


@pytest.mark.parametrize('result', PARAMETERS_LIST_FOR_POP)
def test_pop(result):
    """
    test pop function
    """
    assert MOCK_LINKED_LIST.pop() == result



