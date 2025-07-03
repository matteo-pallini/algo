
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BSTree:

    def __init__(self):
        self.root = None

    def insert_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = prev_node = self.root
            while node:
                prev_node = node
                node = node.left if node.value > value else node.right

            if prev_node.left.value > value:
                prev_node.left = Node(value)
            else:
                prev_node.right = Node(value)

    def search_node(self, value):
        node, _ = self._search_node(value)
        return node

    def _search_node(self, value):
        node = self.root
        while node:
            prev_node = node
            if node.value == value:
                return node, prev_node
            node = node.left if node.value > value else node.right
        return -1, -1

    def delete_node(self, value):
        node, prev_node = self._search_node(value)
        if node == -1:
            return False
        else:
            if node.left is None or node.right is None:
                if node.left is not None:
                    replacement_value, node.left = node.left.value, None
                elif node.right is not None:
                    replacement_value, node.right = node.right.value, None
                else:
                    replacement_value = None

                node.value = replacement_value
            else:
                inorder_successor, prev_successor_node = node.right, node
                while inorder_successor.left:
                    prev_successor_node = inorder_successor
                    inorder_successor = inorder_successor.left

                node.value = inorder_successor.value

                if node.right == inorder_successor:
                    node.right = node.right.right
                else:
                    prev_successor_node.left = None

