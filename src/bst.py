"""
Class definition for a BST
"""
class BSTNode:
    """
    Helper class for BSTNode
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    BST class
    """

    def __init__(self, some_iterable=[]):
        """
        This is the initializer for the BST
        """
        self._root = None
        self._size = 0
        if some_iterable:
            if type(some_iterable) in [list, tuple]:
                for value in some_iterable:
                    self.insert(value)

    def insert(self, value):
        """
        This method is responsible for inserting values into the BST
        """
        if type(value) not in [float, int]:
            raise TypeError("Numbers only.")
        self._size += 1
        self._root = self._insert_helper(self._root, value)

    def size(self):
        """
        This method returns the number of items contained in the BST
        """
        return self._size

    def _insert_helper(self, root, value):
        """
        This function inserts value into BST
        """
        if root is None:
            return BSTNode(value)

        if value < root.value:
            root.left = self._insert_helper(root.left, value)
        elif value > root.value:
            root.right = self._insert_helper(root.right, value)
        return root

    def search(self, value):
        """
        This method returns the node containing the value if it exists, else returns None
        """
        if not self._root:
            raise IndexError("The BST is empty.")
        if type(value) not in [int, float]:
            raise TypeError("Number only")
        if self.contains(value):
            return self._search_helper(self._root, value)
        else:
            return None

    def _search_helper(self, root, value):
        """
        This helper method returns the node containing the value if it exists, else returns None
        """
        if root.value == value:
            return root
        if value < root.value:
            return self._search_helper(root.left, value)
        elif value > root.value:
            return self._search_helper(root.right, value)

    def contains(self, value):
        """
        This method returns a boolean indicating if a value exists in the BST
        """

        return self._contains_helper(self._root, value)

    def _contains_helper(self, root, value):
        """
        This method returns a boolean indicating if a value exists in the BST
        """
        if root is None:
            return False

        if value < root.value:
            return self._contains_helper(root.left, value)
        elif value > root.value:
            return self._contains_helper(root.right, value)

        return root.value == value

    def breadth_first_traversal(self):
        """
        This method traverses the BST in a BFS fashion; That is, it traverses the BST, level by level
        """
        if not self._root:
            raise IndexError("The BST is empty.")
        a_queue = AQueue()
        a_queue.enqueue(self._root)
        a_list = []
        while not a_queue.is_empty():
            a_node = a_queue.dequeue()
            if a_node.left is not None:
                a_queue.enqueue(a_node.left)
            if a_node.right is not None:
                a_queue.enqueue(a_node.right)
            a_list.append(a_node.value)
        for val in a_list:
            yield val

    def inorder_traversal(self):
        """
        This method traverses the BST in an inorder fashion
        """
        a_list = []
        if not self._root:
            raise IndexError("The BST is empty.")
        self._inorder_traversal_helper(self._root, a_list)
        for val in a_list:
            yield val

    def _inorder_traversal_helper(self, root, a_list):
        """
        The method traverses the BST in an inorder fashion
        (Left is visited, Parent is visited, Right is visited)
        """
        if root is not None:
            self._inorder_traversal_helper(root=root.left, a_list=a_list)
            a_list.append(root.value)
            self._inorder_traversal_helper(root=root.right, a_list=a_list)

    def preorder_traversal(self):
        """
        This method traverses the BST in a preorder fashion;
        That is, the Parent is Visited, then Left, then Right
        """
        a_list = []
        if not self._root:
            raise IndexError("The BST is empty.")
        self._preorder_traversal_helper(self._root, a_list)
        for val in a_list:
            yield val

    def _preorder_traversal_helper(self, root, a_list):
        """
        This method traverses the BST in a preorder fashion;
        That is, the Parent is Visited, then Left, then Right
        """
        if root is not None:
            a_list.append(root.value)
            self._preorder_traversal_helper(root=root.left, a_list=a_list)
            self._preorder_traversal_helper(root=root.right, a_list=a_list)

    def postorder_traversal(self):
        """
        This method traverses the BST in a postorder fashion;
        That is, Left is visited, Right is visited, then Parent
        """
        a_list = []
        if not self._root:
            raise IndexError("The BST is empty.")
        self._postorder_traversal_helper(self._root, a_list)
        for val in a_list:
            yield val

    def _postorder_traversal_helper(self, root, a_list):
        """
        This method traverses the BST in a postorder fashion; That is,
        Left is visited, Right is visited, then Parent
        """
        if root is not None:
            self._postorder_traversal_helper(root=root.left, a_list=a_list)
            self._postorder_traversal_helper(root=root.right, a_list=a_list)
            a_list.append(root.value)

    def depth(self):
        """
        This method returns the total number of levels in the BST
        """
        return self._depth_helper(self._root)

    def _depth_helper(self, root):
        """
        This helper method returns the total number of levels in the BST
        """
        if root is None:
            return 0

        return 1 + max(self._depth_helper(root.left), self._depth_helper(root.right))

    def balanced(self):
        """
        This method returns a positive or negative integer that represents how
        well balanced the tree is.
        From Stackoverflow: A well-formed binary tree is said to be "height-balanced",
        if (1) it is empty, or (2) its left and right children are height-balanced
        and the height of the left tree is within 1 of the height of the right tree
        """
        return self._depth_helper(self._root.left) - self._depth_helper(self._root.right)

    def search_for_node_to_remove_and_its_parent(self, parent, root, value):
        """
        This helper method is responsible for finding and returning
        the node to remove and its parent.
        """
        if root is None:
            return None
        if value < root.value:
            parent = root
            return self.search_for_node_to_remove_and_its_parent(parent, root.left, value)
        elif value > root.value:
            parent = root
            return self.search_for_node_to_remove_and_its_parent(parent, root.right, value)
        else:
            return parent, root

    def remove_node_with_zero_children(self, parent, node_to_remove):
        """
        This helper method is responsible for removing a node with zero children
        """
        if node_to_remove is self._root:
            # if node to remove is equal to the root
            # then we are removing the last value in the bst
            self._root = None
            self._size -= 1
            return
        if parent.right is node_to_remove:
            parent.right = None
            self._size -= 1
            return
        else:
            parent.left = None
            self._size -= 1
            return

    def remove_node_with_both_children(self, node_to_remove):
        """
        This helper method is responsible for removing a node that has both children.
        """
        if node_to_remove is self._root:
            # Find the replacement
            # The replacement should be the maximum in the left subtree (if the left subtree exists)
            replacement = node_to_remove.left
            follow_replacement = node_to_remove
            while replacement.right is not None:
                follow_replacement = replacement
                replacement = replacement.right

            # Once the replacement has been found, overwrite the value you want to remove with the value from the replacement
            node_to_remove.value = replacement.value
            # The BST now has duplicate value; The new value at the root and the value at the replacement node;
            # Remove the duplicate by severing follow_replacement.right link to the replacement
            follow_replacement.right = None
            self._size -= 1
            return

            # 1 caveat with this case: if the right subtree does not have a left branch,
            # this means that the minimum value of the right subtree is the root node
            # (the node to be removed)
            # Check for special case
        if node_to_remove.right.left is None:
            node_to_remove.value = node_to_remove.right.value
            node_to_remove.right = node_to_remove.right.right
            self._size -= 1
            return

            # Find the replacement node
        replacement = node_to_remove.right
        follow_replacement = node_to_remove
        # This finds the minimum in the right subtree (if right subtree exists)
        while replacement.left is not None:
            follow_replacement = replacement
            replacement = replacement.left

        # Once the replacement has been found
        # overwrite the value you want to remove with the value from the replacement
        node_to_remove.value = replacement.value
        # The BST now has duplicate values;
        # The new value at the root and the value at the replacement node;
        # Links the right subtree to parent's left
        follow_replacement.left = replacement.right
        self._size -= 1

    def remove_node_with_one_child(self, parent, node_to_remove):
        """
        This helper method is responsible for removing a node with one child.
        """
        # Case 2: The node to be removed has one child
        if node_to_remove.right is None:  # if true, then left subtree contains a child
            if node_to_remove is self._root:
                # Skips over the node to remove and links to its left child
                self._root = self._root.left
                self._size -= 1
                return

            if parent.right is node_to_remove:
                parent.right = node_to_remove.left
                self._size -= 1
                return
            else:
                parent.left = node_to_remove.left
                self._size -= 1
                return
        else:
            # And by process of elimination, the right subtree contains a child
            if node_to_remove is self._root:
                # Skips over the node to remove and links to its right child
                self._root = self._root.right
                self._size -= 1
                return

            if parent.right is node_to_remove:
                parent.right = node_to_remove.right
                self._size -= 1
                return
            else:
                parent.left = node_to_remove.right
                self._size -= 1

    def remove(self, value):
        """
        This method is responsible for removing the given value from the BST.
        """
        # Checks to see if the value is in the BST
        if self.contains(value):
            parent = None
            node_to_remove = None
            parent, node_to_remove = self.search_for_node_to_remove_and_its_parent(parent, self._root, value)
            if node_to_remove.left is None and node_to_remove.right is None:
                self.remove_node_with_zero_children(parent, node_to_remove)
                return

            if node_to_remove.left is not None and node_to_remove.right is not None:
                # The node to remove has both children
                self.remove_node_with_both_children(node_to_remove)
                return
            else:
                # The node_to_remove has at least one child
                self.remove_node_with_one_child(parent, node_to_remove)
