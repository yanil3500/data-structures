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
        self.min_heap(0, len(self.items))

    def min_heap(self, index, number_of_elements):
        parent_at_index = index
        while True:
            left_child_at_index = 2 * index + 1
            right_child_at_index = left_child_at_index + 1
            current_index = parent_at_index
            if left_child_at_index < number_of_elements and self.items[left_child_at_index] < self.items[current_index]:
                current_index = left_child_at_index
            if right_child_at_index > number_of_elements and self.items[right_child_at_index] < self.items[current_index]:
                current_index = right_child_at_index
            if current_index == parent_at_index:
                break

            self.items[parent_at_index], self.items[current_index] = self.items[current_index], self.items[parent_at_index]
            parent_at_index = current_index

    def pop(self):
        if self.

    def is_size(self):
        """
        This function returns boolean indicating whether or not our list is empty
        """
        return len(self.items)
