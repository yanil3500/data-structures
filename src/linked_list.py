"""
A singly-linked list implementation
"""


class Node:
    """
    supporting class for linked list
    """
    def __init__(self, val):
        """."""
        self.val = val
        self.next = None


class LinkedList:
    """
    singly linked list
    """
    head = None
    length = 0
    def __init__(self,values_list=[]):
        """Initialize LinkedList."""
        if len(values_list) > 0:
            """where we create Nodes"""

    def push(self, value):
        """"""
        if self.head == None:
            self.head = Node(value)
            self.length += 1

        else:
            temp_node = Node(value)
            temp_node.next = self.head
            self.head = temp_node
            self.length += 1

    def pop(self):
        """."""
        if self.length > 0:
            temp_node = self.head
            self.head = self.head.next
            self.length -= 1
            return temp_node
        else:
            print('No values to pop.')
            raise TypeError

    def search(self, val):
        if self.length > 0:
            temp_node = self.head
            for i in range(self.length - 1):
                if temp_node.val == val:
                    return temp_node

                else:
                    temp_node = temp_node.next

        return None

    def remove(self, node_to_remove):
        """."""
        pass


    def size(self):
        """."""
        return self.length


def main():
    """
    main function
    """
    print('main function')


if __name__ == '__main__':
    main()
