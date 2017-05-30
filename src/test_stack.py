"""
Test stack module
"""

import pytest

INIT_TABLE = [
    ([1, 2, 3, 'four', 'five'], 5),
    ((999, 12, 'three'), 3),
    ('this string will become a linked list', 37),
    (None, 0),
    (None, 0),
    (None, 0)
]

INIT_ERROR_TABLE = [
    (999),
    (1),
    (.199992999),
    (True),
    (False),
    (object)
]

PUSH_TABLE = [
    ([1, 2, 3, 'four', 'five'], 6),
    ((999, 12, 'three'), 4),
    ('this string will become a linked list', 38)
]

POP_TABLE = [
    ([1, 2, 3, 'four', 'five'], 4),
    ((999, 12, 'three'), 2),
    ('this string will become a linked list', 36)
]

POP_ERROR_TABLE = [
    ([]),
    (''),
    (())
]

LEN_TABLE = [
    ('this is an iterable', 5, 10, 24),
    ([1, 2, 3, 4, 5, 6, 7], 7, 100, 100)
]


@pytest.mark.parametrize('iterable, length', INIT_TABLE)
def test_init(iterable, length):
    """The test_init function tests to see if the stack initializer is in working order."""
    from stack import Stack
    assert len(Stack(iterable)) == length


@pytest.mark.parametrize('non_iterable', INIT_ERROR_TABLE)
def test_init_error(non_iterable):
    """The test_init_error evaluates whether or not a TypeError has been raised."""
    from stack import Stack
    with pytest.raises(TypeError):
        Stack(non_iterable)


@pytest.mark.parametrize('iterable, length', PUSH_TABLE)
def test_push(iterable, length):
    """The test_push function checks to see if items are being push onto the stack."""
    from stack import Stack
    stack = Stack(iterable)
    stack.push(1)
    assert len(stack) == length


@pytest.mark.parametrize('iterable, length', POP_TABLE)
def test_pop(iterable, length):
    """The test_pop function ensures that items are being removed from the top of the stack."""
    from stack import Stack
    stack = Stack(iterable)
    stack.pop()
    assert len(stack) == length


@pytest.mark.parametrize('non_iterable', POP_ERROR_TABLE)
def test_pop_error(non_iterable):
    """The test_pop_error function ensures that an IndexException is raised when attempting to pop() items from an empty stack."""
    from stack import Stack
    with pytest.raises(IndexError):
        Stack(non_iterable).pop()


@pytest.mark.parametrize('iterable, num_of_pops, num_of_pushes, length', LEN_TABLE)
def test_len(iterable, num_of_pops, num_of_pushes, length):
    """The test_len function checks to see if the len() function returns the proper length."""
    from stack import Stack
    stack = Stack(iterable)

    for i in range(num_of_pops):
        stack.pop()

    for i in range(num_of_pushes):
        stack.push(i)

    assert len(stack) == length
