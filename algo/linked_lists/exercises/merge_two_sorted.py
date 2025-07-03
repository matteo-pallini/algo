class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_two_sorted(sorted_one, sorted_two):
    new, first, second = Node(data=None), sorted_one, sorted_two
    new_start = new

    while first and second:
        if first.data < second.data:
            new.next = first
            first = first.next
        else:
            new.next = second
            second = second.next
        new = new.next
        new.next = None
    if first:
        new.next = first
    if second:
        new.next = second
    return new_start.next
