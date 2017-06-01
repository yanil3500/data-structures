"""
Implementation of Heap Class
"""


class BinaryHeap:
    """
    This is a class declaration for a binary heap
    """
    def __init__(self, some_iterable=[]):
        """
        This method creates an instance of the BinaryHeap class.
        """
        self.items = []
        if some_iterable:
            for value in range(some_iterable):
                self.items.push(value)

    def push(self, value):
        """
        This function is responsible for adding elements to our heap.
        """
        self.items.append(value)
        self.bubble_up(len(self.items) - 1)

    def bubble_up(self, index):
        """
        The bubble_up method is responsible for 
        """
        while self.items[index] < self.items[self.parent_index(index)]:
            self.items[index], self.items[self.parent_index(index)] = self.items[self.parent_index(index)], self.items[index]
            index = self.parent_index(index)

    def left_child_index(self, index):
        """
        Calculates the index of the left child of a given parent
        """
        return 2 * index + 1

    def right_child_index(self, index):
        """
        Calculates the index of the right child of a given parent
        """
        return self.left_child_index(index) + 1

    def parent_index(self, index):
        """
        This method calculates the index of the parent value
        """
        return int((index - 1) / 2)


    def size(self):
        """
        This function returns the number of elements within the heap
        """
        return len(self.items)

    def pop(self):
        if self.size() == 0:
            return None
        elif self.size() == 1:
            return self.items.pop()
        else:
            root_value = self.items[0]
            self.items[0] = self.items.pop()
            self.min_heapify()
            return root_value

    def min_heapify(self):
        for i in range(len(self.items)):
            if self.right_child_index(i) < len(self.items):
                if self.items[self.left_child_index(i)] < self.items[self.parent_index(i)]:
                    self.items[self.parent_index(i)], self.items[self.left_child_index(i)] = self.items[self.left_child_index(i)], self.items[self.parent_index(i)]
                    if self.items[self.right_child_index(i)] < self.items[self.parent_index(i)]:
                        self.items[self.parent_index(i)], self.items[self.right_child_index(i)] = self.items[self.right_child_index(i)], self.items[self.parent_index(i)]
                elif self.items[self.right_child_index(i)] < self.items[self.parent_index(i)]:
                    self.items[self.parent_index(i)], self.items[self.right_child_index(i)] = self.items[self.right_child_index(i)], self.items[self.parent_index(i)]
                    if self.items[self.left_child_index(i)] < self.items[self.parent_index(i)]:
                            self.items[self.parent_index(i)], self.items[self.left_child_index(i)] = self.items[self.left_child_index(i)], self.items[self.parent_index(i)]


def main():
    """
    for testing purposes
    """
    a_heap = BinaryHeap()

    for value in [7, 2, 6, 5, 10, -1, 4, 6]:
        a_heap.push(value)

    print('The heap: {}'.format(a_heap.items))

    a_str = 'All values in min_heap: '

    while a_heap.size() > 0:
        a_str += '{}, '.format(a_heap.pop())
        print('After min-heapify: {}'.format(a_heap.items))

    print(a_str)





if __name__ == "__main__":
    main()
