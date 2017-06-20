"""
Queue class declaration
"""


class Node:  # pragma: no cover
    def __init__(self, value):
        """
        This is the initializer for the Node supporting class.
        """
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        """
        This is the initializer for the Queue class.
        """
        self._front = self._rear = None
        self._length = 0

    def enqueue(self, value):
        """
        The enqueue method adds items to our queue.
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
        The dequeue method removes items from the queue in the order in which they were added.
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
        The size method returns the size of the queue.
        """
        return self._length

    def is_empty(self):
        """
        This method returns a boolean indicating whether or not the queue is empty
        """
        return self._length == 0
        
    def peek(self):
        """
        The peek method retunrs the next value in queue; The peek method returns None if the queue is empty.
        """
        if not self._front:
            return None
        else:
            return self._front.value

    def __len__(self):  # pragma: no cover
        """
        Defining the __len__ method for our Queue enables us to use the built-in len function.
        """
        return self.size()
