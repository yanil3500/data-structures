"""Implementation of a priority queue."""
import sys


class PriorityQ:
    def __init__(self):
        """Initialize the PriorityQ."""
        self.items = []


    def insert(self, value, priority=sys.maxsize):
        """Insert a value into our priority queue with an optional priority."""
        self.items.append((value, priority))
        self.bubble_up()


    def pop(self):
        """Pop the most important value in our priority queue.
        If we have more than one value with the hightest priority, we take the first value in the priority queue. """
        if len(self.items) == 0:
            raise IndexError('Priority Queue is empty.')

        root_value = self.items[0][0]

        if len(self.items) == 1:
            self.items = []
            return root_value

        self.items[0] = self.items[len(self.items) - 1]
        self.items.pop()
        self.bubble_down()
        return root_value


    def peek(self):
        """Return the most important value in our priority queue.
        If we have more than one value with the hightest priority, we return the first value in the priority queue. """
        pass


    def bubble_up(self):
        """Perform a bubble-up operation after a insert operation."""
        current_index = len(self.items) - 1
        parent_index = self.get_parent_index(current_index)

        while self.items[parent_index][1] > self.items[current_index][1]:
            self.items[parent_index], self.items[current_index] = self.items[current_index], self.items[parent_index]
            current_index = parent_index
            parent_index = self.get_parent_index(current_index)


    def bubble_down(self):
        """Perform a bubble-down operation after pop operation."""
        current_index = self.items[0]
        left_child_index = self.get_left_child(current_index)
        right_child_index = self.get_right_child(current_index)

        while left_child_index < len(self.items):
            while right_child_index < len(self.items):
                # we have two children to compare


            # we have a left child to compare



    def get_parent_index(self, child_index):
        """Return parent index of child index."""
        return int((child_index - 1) / 2)


    def get_left_child(self, parent_index):
        """Return left child of parent index."""
        return (2 * parent_index) + 1


    def get_right_child(self, parent_index):
        """Return right child of parent index."""
        return (2 * parent_index) + 2


if __name__ == '__main__':
    pq = PriorityQ()
    pq.insert(4, 10)
    pq.insert(6, 2)
    pq.insert(43, 7)
    pq.insert(100)
    pq.insert(50, 0)
    pq.pop()

    print(pq.items)