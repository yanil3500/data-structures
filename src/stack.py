"""
implementation of a stack
"""
from linked_list import LinkedList


class Stack(object):

    def __init__(self, iterable=None):
        if type(iterable) in [list, tuple, str]:
            self._container = LinkedList(iterable=iterable)

        elif iterable is None:
            self._container = LinkedList()

        else:
            raise TypeError('You need to use an iterable or no arguments.')

    def push(self, value):
        """
        The push method on our stack uses the linked list's push function as the underlying method by which items are added onto our stack.
        """
        self._container.push(value)

    def pop(self):
        """
        The pop method on our stack uses the linked list's pop function as the underlying method by which items are removed from the stack.
        """
        return self._container.pop()

    def __len__(self):
        """
        This function definition allows for the built-in len func to be used.
        """
        return self._container.length


