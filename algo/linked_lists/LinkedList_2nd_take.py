class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def search_node(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

    def delete_node(self, value):
        if self.head is None:
            return -1
        else:
            node = self.search_node(value)
            if node:
                if not node.prev:
                    self.head, node.next.prev = node.next, None
                elif node.prev and node.next:
                    node.prev.next, node.next.prev = node.next, node.prev
                else:
                    node.prev.next = None

