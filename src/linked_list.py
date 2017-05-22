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


class LinkedList:
    """
    singly linked list
    """
    head = None
    length = 0
    def __init__(self,values_list=[]):
        if len(values_list) > 0:
            """where we create Nodes"""

    def push(self, value):
        if head == None:
            temp_node = Node(value)
            head = temp_node
            self.length += 1

        else:
            temp_node = Node(value)
            temp_node.next = self.head
            self.head = temp_node
            self.length += 1

def main():
    """
    main function
    """
    print('main function')


if __name__ == '__main__':
    main()
