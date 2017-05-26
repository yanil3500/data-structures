"""
Queue class declaration
"""


def main():
    """
    the main function
    """
    pass

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
            if not self._front:
                self._front = self._rear = Node(value)
                self._length += 1
            else:
                self._rear.next = Node(value)
                self._rear = self._rear.next
                self._length += 1

    





if __name__ == "__main__":
    main()
