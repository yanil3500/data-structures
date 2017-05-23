"""
implementation of a stack
"""
from linked_list import LinkedList


class Stack(object):

    def __init__(self, iterable=None):
        if type(iterable) in [list, tuple, str]:
            self._container = LinkedList(iterable=iterable)

        else:
            self._container = LinkedList()


    def push(self, value):
        """
        uses the linked list as the underlying data structure
        """
        self._container.push(value)

    def pop(self):
        """
        uses the linked list as the underlying data structure,
        """
        return self._container.pop()

    def __len__(self):
        """
        allows for the built-in len func
        """
        return self._container.length


def main():
    """
    main function
    """
    a_stack = Stack([1, 2, 3, 4, 5, 'A', 'B'])
    print(dir(a_stack))



if __name__ == '__main__':
    main()

