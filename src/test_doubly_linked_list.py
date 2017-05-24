"""
Tests for doubly linked list
"""
import pytest

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
    ([10, 11, 23, 45, 6, 7, 8, 9, 10], 3, 6)
]


@pytest.fixture
def test_empty_dll():
    """
    prepare an empty dll for testing purposes
    """
    from doubly_linked_list import DoublyLinkedList
    a_test_dll = doubly_linked_list()
    return a_test_dll


def test_init_for_doubly_linked_list_length(test_empty_dll):
    """
    tests to make sure that a recently initialized dll is empty
    """
    assert test_empty_dll.length == 0


def test_init_for_doubly_linked_list_previous_property(test_empty_dll):
    """
    tests to make sure that a recently initialized dll has its previous property set to None
    """
    assert test_empty_dll.previous is None


def test_init_for_doubly_linked_list_next_property(test_empty_dll):
    """
    tests to make sure that a recently initialized dll has its next property set to None
    """
    assert test_empty_dll.previous is None


@pytest.mark.parametrize('value, result', PARAMETERS_LIST_FOR_PUSH)
def test_push(value, result):
    """
    tests to see if values are added to dll by checking the dll length 
    after pushing the values
    """
    from doubly_linked_list import DoublyLinkedList
    test_dll = DoublyLinkedList()
    test_dll.push(value)
    assert test_dll.length == result

@pytest.mark.parametrize('values, number_of_items_to_remove, result', PARAMETERS_LIST_FOR_PUSH)
def test_pop(values, number_of_items_to_remove, result):
    """
    tests to see if values are removed to dll by checking the dll length
    after popping the values off
    """
    from doubly_linked_list import DoublyLinkedList
    test_dll = DoublyLinkedList()

    for value in values:
        test_dll.push(value)
    for i in range(1, number_of_items_to_remove):
        test_dll.pop()

    assert test_dll.length == result

