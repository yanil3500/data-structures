"""This module implements the deque ADT."""
from doubly_linked_list import DoublyLinkedList


class Deque(DoublyLinkedList):
    """Deque class."""
    def __init__(self):
        """Deque constructor"""
        DoublyLinkedList.__init__(self)

    def append(self, value):
        """adds value to the end of the deque"""
        DoublyLinkedList.append(self, value)

    def appendleft(self, value):
        """adds a value to the front of the deque"""
        DoublyLinkedList.push(self, value)

    def pop(self):
        """removes a value from the end of the deque and
        returns it (raises an exception if the deque is empty)"""
        return DoublyLinkedList.shift(self)

    def popleft(self):
        """removes a value from the front of the deque and
        returns it (raises an exception if the deque is empty)"""
        return DoublyLinkedList.pop(self)

    def peek(self):
        """returns the next value that would be returned by pop
        but leaves the value in the deque (returns None if the deque is empty)"""
        if self.size() > 0:
            return self.tail.value
        else:
            return None

    def peekleft(self):
        """returns the next value that would be returned by popleft
        but leaves the value in the deque (returns None if the deque is empty)"""
        if self.size() > 0:
            return self.head.value
        else:
            return None

    def size(self):
        """returns the count of items in the queue (returns 0 if the queue is empty)"""
        return DoublyLinkedList.__len__(self)
