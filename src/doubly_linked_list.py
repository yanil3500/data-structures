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
        """Push a value to doubly linked list."""
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1

        else:
            temp_node = Node(value)
            self.head.previous = temp_node
            temp_node.next = self.head
            self.head = temp_node
            self.head.previous = None
            self.length += 1


    def append(self, value):
        """Append a value to end of doubly linked list."""
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1

        else:
            new_node = Node(value)
            new_node.previous = self.tail
            new_node.next = None
            self.tail.next = new_node
            new_node = self.tail
            self.length += 1



    def pop(self):
        """Pop value from front of DoublyLinkedList."""
        if self.length > 0:
            temp_node = self.head
            self.head = self.head.next

            if self.head != None:
                self.head.previous = None

            self.length -= 1
            return temp_node.value

        else:
            raise IndexError('Does not contain anymore elements. Cannot remove non-existing elements.')

    def shift(self):
        """Shift last value from doubly linked list"""
        if self.head != None:
            if self.head == self.tail:
                self.pop()

            else:
                self.tail.previous.next = None
                self.tail.next = None
                self.tail = self.tail.previous
                self.length -= 1

        else:
            raise AttributeError

    def remove(self, value):
        """Remove a node from DoublyLinkedList and return True."""
        if self.head != None:
            if self.head.value == value:
                self.pop()

            elif self.head == self.tail:
                self.shift()

            else:
                print(self.head)
                previous_node = self.head
                current_node = self.head.next
                print(current_node.previous)
                while current_node != None:
                    if current_node.value == value:
                        if current_node.value == self.tail.value:
                            self.shift()
                            return

                        else:
                            current_node.previous.next = current_node.next
                            current_node.next.previous = current_node.previous
                            current_node.next = None
                            current_node.previous = None
                            self.length -= 1
                            return

                    else:
                        previous_node = current_node
                        current_node = current_node.next

                raise IndexError # If value is not present, it will raise an appropriate Python exception.

        else:
            raise IndexError # empty DoublyLinkedList


    def __len__(self):
        return self.length


    def display(self):
        """Return a unicode string representation of LinkedList."""
        if self.length > 0:
            linked_list_string = '('
            temp_node = self.head
            while temp_node != None:
                linked_list_string += '{},'.format(temp_node.value)
                temp_node = temp_node.next

            linked_list_string = linked_list_string[:-1]
            linked_list_string += ')'

            return linked_list_string


def main(): # pragma: no cover
    pass


main() # pragma: no cover