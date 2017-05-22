"""
A singly-linked list implementation
"""


class Node:
    """
    supporting class for linked list
    """
    def __init__(self, val):
        """Initialize a Node with a given value"""
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
            for i in range(len(values_list)):
                self.push(values_list[i])


    def push(self, value):
        """Push value to front of LinkedList."""
        if self.head == None:
            self.head = Node(value)
            self.length += 1

        else:
            temp_node = Node(value)
            temp_node.next = self.head
            self.head = temp_node
            self.length += 1

    def pop(self):
        """Pop value from front of LinkedList."""
        if self.length > 0:
            temp_node = self.head
            self.head = self.head.next
            self.length -= 1
            return temp_node
        else:
            print('No values to pop.')
            raise TypeError

    def search(self, val):
        """Return the node of a given value."""
        if self.length > 0:
            temp_node = self.head

            while (temp_node != None):
                if temp_node.val == val:
                    return temp_node
                else:
                    temp_node = temp_node.next

        return None

    def remove(self, node_to_remove):
        """Remove a node from LinkedList and return True."""
        if self.length > 0:
            previous_node = self.head
            temp_node = self.head.next

            if previous_node == node_to_remove:
                self.head = self.head.next
                previous_node.next = None
                self.length -= 1
                return True


            while temp_node != None:
                if temp_node == node_to_remove:
                    previous_node.next = temp_node.next
                    node_to_remove = None
                    self.length -= 1
                    return True

                else:
                    previous_node = temp_node
                    temp_node = temp_node.next

            return False


    def __len__(self):
        """Return length of LinkedList."""
        return self.length

    def display(self):
        """Return a unicode string representation of LinkedList."""
        if self.length > 0:
            linked_list_string = '('
            temp_node = self.head
            while temp_node != None:
                linked_list_string += '{},'.format(temp_node.val)
                temp_node = temp_node.next

            linked_list_string = linked_list_string[:-1]
            linked_list_string += ')'

            return linked_list_string

    def __str__(self):
        """."""
        return self.display()


def main(): # pragma: no cover
    """
    main function
    """
    print('main function')


if __name__ == '__main__': # pragma: no cover
    main()
