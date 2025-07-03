
class Node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(val=value)

        node, prev_node = self.root, None
        while node:
            if node.val > value:
                node, prev_node = node.left, node
            else:
                node, prev_node = node.right, node

        if prev_node.val > value:
            prev_node.left = Node(value)
        else:
            prev_node.right = Node(value)

    def _search_node(self, value):
        node, prev_node = self.root, None
        while node:
            if node.val == value:
                return node, prev_node
            elif node.val > value:
                prev_node, node = node, node.left
            else:
                prev_node, node = node, node.right
        return -1, -1

    def delete(self, value):
        node, prev_node = self._search_node(value)

        if node == -1:
            return -1

        if node.left is None or node.right is None:
            if node.left is not None:
                node.val, node.left = node.left.val, None
            elif node.right is not None:
                node.val, node.right = node.right.val, None
            else:
                if prev_node.left.val == node.val:
                    prev_node.left = None
                else:
                    prev_node.right = None
        else:

