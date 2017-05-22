"""
A singly-linked list implementation
"""


class Node:
    """
    supporting class for linked list
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class Singly_Linked_List:
    """
    singly linked list
    """
    head = None
    length = 0


if __name__ == '__main__':
    main()