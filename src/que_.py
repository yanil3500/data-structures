"""
Queue class declaration
"""


def main(): # pragma: no cover
    """
    the main function
    """
    a_queue = Queue()

    # add elements to queu
    for value in 'cash-rules-everthing-around-me':
        a_queue.enqueue(value)

    print(a_queue)
    print('peek(): {}'.format(a_queue.peek()))
    print('size(): {}'.format(a_queue.size()))
    wutang = ''

    a_queue.make_it_empty()

    print(a_queue)
    print(wutang)
    print('peek(): {}'.format(a_queue.peek()))
    print('size(): {}'.format(a_queue.size()))
    # a_queue.dequeue()


class Node: # pragma: no cover
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
        try:
            if self._front is self._rear and self._front is not None:
                removed_item = self._front
                self._front = self._rear = None
                removed_item.next = None
                self._length -= 1
                return removed_item.value
            if self._length > 0:
                removed_item = self._front
                self._front = self._front.next
                removed_item.next = None
                self._length -= 1
                return removed_item.value
        except IndexError:
            raise IndexError("Cannot remove elements from empty queue.")
        else:
            raise IndexError("Cannot remove elements from empty queue.")

    def __str__(self):
        """
        generates a string representing the queue
        """
        if self._front is not None:
            a_string = '[front]'
            current = self._front
            while current.next is not None:
                a_string += '->[{}]'.format(current.value)
                current = current.next
            a_string += '[{}]->'.format(current.value)
            a_string += '[rear]'
            return a_string
        else:
            return 'The state of the queue: front - {}, last -{}'.format(self._front, self._rear)

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

    def __len__(self):
        """
        return the number of elements in queue
        """
        return self.size()

    def make_it_empty(self):
        """
        empties the queue
        """
        while self.size() > 0:
            self.dequeue()


if __name__ == "__main__":
    main()
