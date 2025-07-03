class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BSTree:

    def __init__(self):
        self.root = None

    def insert_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            node = last_node = self.root
            while node:
                last_node = node
                node = node.left if value <= node.value else node.right

            if value <= last_node.value:
                last_node.left = Node(value)
                last_node.left.parent = last_node
            else:
                last_node.right = Node(value)
                last_node.right.parent = last_node

    def search_node(self, value):
        return self._search_value(value)

    def _search_value(self, value):
        node = self.root
        while node:
            if value == node.value:
                return node
            node = node.left if node.value > value else node.right
        return None

    def delete_node(self, value):
        """Handle 3 possible cases:
        - 1. 0 child -> delete node
        - 2. 1 child -> replace node with child data
        - 3. 2 children -> find node inorder successor or predecessor and replace the data
        """
        node = self._search_value(value)
        if node:
            # handle case 1 and 2
            if node.left is None or node.right is None:
                if node.left is not None:
                    replacement_node_val, node.left = node.left.value, None
                elif node.right is not None:
                    replacement_node_val, node.right = node.right.value, None
                else:
                    replacement_node_val = None
                node.value = replacement_node_val
            # handle 3rd case
            else:
                inorder_successor = node.right
                while inorder_successor.left:
                    inorder_successor = inorder_successor.left

                node.value = inorder_successor.value
                # if the right child has only right children we just spline the right child
                if inorder_successor == node.right:
                    node.right = node.right.right
                # otherwise we use the inorder_successor parent
                else:
                    inorder_successor.parent.left = None