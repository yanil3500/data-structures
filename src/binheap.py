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
        self.length = 0
        if some_iterable:
            for value in some_iterable:
                self.push(value)

    def push(self, value):
        """
        This function is responsible for adding elements to our heap.
        """
        self.items.append(value)
        self.length += 1
        self.bubble_up(len(self.items) - 1)

    def swap(self, first_index, second_index):
        """
        This function will be responsible for swapping the values at the indices that are passed in.
        """
        self.items[first_index], self.items[second_index] = self.items[second_index], self.items[first_index]

    def bubble_up(self, index):
        """
        The bubble_up method will restore the min-heap property if it is disturbed.
        """
        while self.items[self.parent_index(index)] > self.items[index]:
            self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def left_child_index(self, index):
        """
        This function calculates the index of the left child of a given parent index
        """
        return 2 * index + 1

    def right_child_index(self, index):
        """
        This function calculates the index of the right child of a given parent index
        """
        return self.left_child_index(index) + 1

    def parent_index(self, index):
        """
        This method calculates the index of the parent 
        """
        return int((index - 1) / 2)

    def pop(self):
        """
        This method is responsible for removing the minimum value from our heap.
        """
        if self.length == 0:
            raise IndexError('Cannot remove items from an empty heap.')
        if self.length == 1:
            self.length -= 1
            return self.items.pop()
        # Store the min-value (root)
        root_value = self.items[0]
        # Removes the last item in our heap and places it at the beginning
        self.items[0] = self.items.pop()
        # Calls the min_heapify method to restore the min-heap property (that is, both children must have values greater than their parent)
        self.length -= 1
        self.min_heapify()
        return root_value

    def min_heapify(self, index=0):
        # Assign the index into a min_index variable; I'm assuming the index being passed in maps to the smallest value in our heap.
        min_index = index
        # We'll get the indices for the children of the parent index that passed in
        left_child_index = self.left_child_index(index)
        right_child_index = left_child_index + 1
        # The self.right_child_index(index) < self.length condition check ensures that our indices do not go out of range
        if self.right_child_index(index) < self.length:
            # We first determine if the value at the left_child_index is less than the value at the right_child_index
            if left_child_index < self.length and self.items[left_child_index] < self.items[right_child_index]:
                # if true, left_child_index is the location in our heap that has our minimum value 
                min_index = left_child_index
        # Then, we check if the value at the right child index is less than the value at our min_index
            if right_child_index < self.length and self.items[right_child_index] < self.items[min_index]:
            #if true, right_child_index is the location in our heap that has our minimum value
                min_index = right_child_index
        if self.left_child_index(index) < self.length:
            if self.items[left_child_index] < self.items[min_index]:
                min_index = left_child_index
        
        # if the min_index is not equal to the index that is passed in.
        # we'll swap the values at the indices, min_index and index
        # then we'll recursively call our function until our condition evaluates to false
        if min_index != index:
            self.swap(index, min_index)
            self.min_heapify(min_index)

