"""
Queue class declaration
"""


class Node:  # pragma: no cover
    def __init__(self, value):
        """
        initializer for node supporting class
        """
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        """
        initializer for queue class
        """
        self._front = self._rear = None
        self._length = 0

    def enqueue(self, value):
        """
        adds elements to the queue
        """
        if not self._front:
            self._front = self._rear = Node(value)
            self._length += 1
        else:
            self._rear.next = Node(value)
            self._rear = self._rear.next
            self._length += 1

    def dequeue(self):
        """
        removes the elements in the order in which they were added
        """
        if self._front is self._rear and self._front is not None:
            removed_item = self._front
            self._front = self._rear = None
            self._length -= 1
            return removed_item.value
        if self._length > 0:
            removed_item = self._front
            self._front = self._front.next
            self._length -= 1
            return removed_item.value
        else:
            raise IndexError("Cannot remove elements from empty queue.")

    def size(self):
        """
        returns the size of the list
        """
        return self._length

    def peek(self):
        """
        returns the next value in queue; returns None
        """
        if not self._front:
            return None
        else:
            return self._front.value

    def __len__(self):  # pragma: no cover
        """
        return the number of elements in queue
        """
        return self.size()
