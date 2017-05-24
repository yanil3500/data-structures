"""
A doubly-linked list implementation
"""


class Node:
    """
    supporting class for linked list
    """
    def __init__(self, val):
        """Initialize a Node with a given value"""
        self.val = val
        self.next = None
        self.previous = None

class doubly_linked_list:
    """doubly_linked_list"""

    head = None
    tail = None
    length = 0

    def __init__(self):
        """doubly_linked_list constructor"""

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            self.length += 1

        else:
            temp_node = self.head
            self.head = Node(value)
            self.head.next = temp_node