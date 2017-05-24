"""
A doubly-linked list implementation
"""


class Node:
    """
    supporting class for linked list
    """
    def __init__(self, value):
        """Initialize a Node with a given value"""
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    """DoublyLinkedList"""

    def __init__(self):
        """DoublyLinkedList"""
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1

        else:
            temp_node = Node(value)
            temp_node.next = self.head
            self.head = temp_node
            self.length += 1

    def pop(self):
        """Pop value from front of DoublyLinkedList."""
        if self.length > 0:
            temp_node = self.head
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return temp_node
        else:
            raise IndexError('Does not contain anymore elements. Cannot remove non-existing elements.')

    def __len__(self):
        return self.length


def main():
    doubly_linked_list = DoublyLinkedList()

main()