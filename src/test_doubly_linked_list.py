"""
Tests for doubly linked list
"""
import pytest
from doubly_linked_list import DoublyLinkedList
PARAMETERS_LIST_FOR_PUSH = [
    (1, 1),
    (100, 2),
    (3, 3),
    (5, 4),
    (7, 5),
    (6, 6)
]

PARAMETERS_LIST_FOR_POP = [
    ([2, 3, 5, 6], 2, 2),
    ([4], 1, 0),
    ([10, 11, 23, 45, 6, 7, 8, 9, 10], 3, 6),
    ([10, 12, 13, 45, 6, 7, 8, 9], 8, 0),
    (['a', 'b', 'l', 'e', 'a', 'k', 'r'], 2, 5),
    (['A', 'B', 'C', 'E', 'F', 'Q'], 3, 3)
]

PARAMETERS_LIST_FOR_POP_EXCEPTION = [
    ([1, 2, 4, 5], 4),
    ([1], 1),
    ([1, 2, 4], 3),
    ([1, 2, 4, 5, 6], 5),
    ([1, 2, 4, 5, 9, 10, 11], 7),
    ([], 0),
]

MOCK_DLL = DoublyLinkedList()


def helper_teardown(a_list):
    """
    resets the dll mock
    """
    a_list.head = a_list.tail = None
    a_list.length = 0

# @pytest.fixture()
# def test_empty_dll():
#     """
#     prepare an empty dll for testing purposes
#     """
#     from doubly_linked_list import DoublyLinkedList
#     a_test_dll = DoublyLinkedList()
#     return a_test_dll




def test_init_for_doubly_linked_list_length():
    """
    tests to make sure that a recently initialized dll is empty
    """
    from doubly_linked_list import DoublyLinkedList
    a_test_dll = DoublyLinkedList()
    assert a_test_dll.length == 0


def test_init_for_doubly_linked_list_tail_property():
    """
    tests to make sure that a recently initialized dll has its tail property set to None
    """
    from doubly_linked_list import DoublyLinkedList
    a_test_dll = DoublyLinkedList()
    assert a_test_dll.tail is None


def test_init_for_doubly_linked_list_head__property():
    """
    tests to make sure that a recently initialized dll has its head property set to None
    """
    from doubly_linked_list import DoublyLinkedList
    a_test_dll = DoublyLinkedList()
    assert a_test_dll.head is None


@pytest.mark.parametrize('value, result', PARAMETERS_LIST_FOR_PUSH)
def test_push(value, result):
    """
    tests to see if values are added to dll by checking the dll length 
    after pushing the values
    """
    MOCK_DLL.push(value)
    assert MOCK_DLL.length == result


@pytest.mark.parametrize('values, number_of_items_to_remove, result', PARAMETERS_LIST_FOR_POP)
def test_pop(values, number_of_items_to_remove, result):
    """
    tests to see if values are removed to dll by checking the dll length
    after popping the values off
    """
    helper_teardown(MOCK_DLL)
    for value in values:
        MOCK_DLL.push(value)

    counter = 0
    while counter < number_of_items_to_remove:
        MOCK_DLL.pop()
        counter += 1
    assert MOCK_DLL.length == result


@pytest.mark.parametrize('values, number_of_items_to_remove', PARAMETERS_LIST_FOR_POP_EXCEPTION)
def test_pop_raise_index_exception(values, number_of_items_to_remove):
    """
    tests to make sure that pop raises an index exception when trying to remove elements from empty list
    """
    helper_teardown(MOCK_DLL)
    for value in values:
        MOCK_DLL.push(value)
    counter = 0
    while counter < number_of_items_to_remove:
        MOCK_DLL.pop()
        counter += 1
    with pytest.raises(IndexError):
        MOCK_DLL.pop()
