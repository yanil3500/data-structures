"""
Queue class declaration
"""


def main():
    """
    the main function
    """
    a_queue = Queue()

    # add elements to queu
    for value in 'cash-rules-everthing-around-me':
        a_queue.enqueue(value)

    while a_queue.size() > 0:
        val = a_queue.dequeue()
        print('dequeue(): {}'.format(val))


class Node:
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
            if self._length > 0:
                if self._front is self._rear:
                    removed_item = self._front
                    self._front = self._rear = None
                    removed_item.next = None
                    self._length -= 1
                    return removed_item.value
                else:
                    removed_item = self._front
                    self._front = self._front.next
                    removed_item.next = None
                    self._length -= 1
                    return removed_item.value
        except:
            raise IndexError("Cannot remove elements from empty queue.")

    def __str__(self):
        """
        generates a string representing the queue
        """
        a_string = '[front]'
        current = self._front
        while current.next is not None:
            a_string += '->[{}]'.format(current.value)
            current = current.next
        a_string += '[{}]->'.format(current.value)
        a_string += '[rear]'
        return a_string

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


if __name__ == "__main__":
    main()
