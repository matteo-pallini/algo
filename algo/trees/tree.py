class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Tree:

    def __init__(self):
        self.root = None

    def insert_value(self, value):
        """insert values so that the tree is kept balanced"""
        if self.root is None:
            self.root = Node(value)
        else:
            queue = [self.root]
            while queue:
                next_elem = queue.pop(0)
                if next_elem.left is None:
                    next_elem.left = Node(value)
                    next_elem.left.parent = next_elem
                    break
                elif next_elem.right is None:
                    next_elem.right = Node(value)
                    next_elem.right.parent = next_elem
                    break
                else:
                    queue.extend([next_elem.left, next_elem.right])