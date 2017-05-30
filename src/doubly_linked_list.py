class Node:
    """
    This is an implementation of a node class.
    """
    def __init__(self, value):
        """
        The __init__ method creates an instance of the Node class when called. The Node class is used a supporting class in our Doubly Linked List implementation.
        """
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    """
    This is an implementation of a doubly linked list.
    """
    def __init__(self):
        """
        The __init__ method creates an instance of the DoublyLinkedList class when called.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        """
        The push method adds value to the beginning of the doubly linked list.
        """
        if self.head is None:
            self.length += 1
            self.head = self.tail = Node(value)
        else:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.length += 1

    def pop(self):
        """
        The pop method removes the first value from the doubly linked list and returns it.
        """
        try:
            if self.head is self.tail:
                removed = self.head
                self.head = self.tail = None
                self.length -= 1
                return removed.value
            removed = self.head
            removed.prev = None
            self.head = self.head.next
            removed.next = None
            self.length -= 1
            return removed.value
        except:
            raise IndexError("""Does not contain anymore elements.
                Cannot remove non-existing elements.""")

    def append(self, value):
        """
        The append method adds values to end of the list.
        """
        if self.head is None:
            self.head = self.tail = Node(value)
            self.length += 1
        else:
            new_item = Node(value)
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
            self.length += 1

    def __len__(self):
        """
        __len__ returns the length of the doubly linked list.
        """
        return self.length

    def shift(self):
        """
        The shift method removes the last value from the list.
        """
        try:
            if self.tail is self.head:
                removed = self.head
                self.head = self.tail = None
                self.length -= 1
                return removed.value
            removed = self.tail
            self.tail = self.tail.prev
            removed.prev = None
            self.tail.next = None
            self.length -= 1
            return removed.value
        except:
            raise IndexError("""Does not contain anymore elements.
                Cannot remove non-existing elements.""")

    def remove(self, val):
        """
        searches for given value then removes it
        """
        if self.head is None:
            return None
        elif self.head.value == val:
            return self.pop()
        elif self.tail.value == val:
            return self.shift()
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                if current.value == val:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    current.prev = current.next = None
                    self.length -= 1
                    return current.value
            else:
                raise LookupError("""Value not found.""")
