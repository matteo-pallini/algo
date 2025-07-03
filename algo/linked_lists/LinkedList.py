import copy


class LinkedList:

    def __init__(self, d):
        self.head = Node(d)
        self.tail = self.head

    def add_element(self, d):
        self.tail.append_to_node(d)
        self.tail = self.tail.next

    def delete_head(self):
        self.head = self.head.next
        self.head.prev.delete_node()

    def delete_tail(self):
        self.tail = self.tail.prev
        self.tail.next.delete_node()

    def get_size(self):
        counter = 1
        node = self.head
        while node.next is not None:
            counter += 1
            node = node.next
        return counter

    def get_values(self):
        pointer = self.head
        values = [pointer.data]
        while pointer.next is not None:
            values.append(pointer.next.data)
            pointer = pointer.next
        return values


class Node:

    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None

    def append_to_node(self, d):
        node = Node(d)
        if self.next is not None:
            node.next = copy.deepcopy(self.next)
        node.prev = self
        self.next = node

    def prepend_to_node(self, d):
        node = Node(d)
        if self.prev is not None:
            node.prev = copy.deepcopy(self.prev)
        node.next = self
        self.prev = node

    def delete_node(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
