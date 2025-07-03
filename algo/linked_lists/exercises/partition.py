from linked_lists.LinkedList import Node, LinkedList

EMPTY_NODE = " "


def partition(ll: LinkedList, cutoff: int):
    first_pointer = ll.head
    while first_pointer is not None and first_pointer.data != EMPTY_NODE:
        if first_pointer.data >= cutoff:
            second_pointer = first_pointer
            next_data = second_pointer.data
            while second_pointer.next is not None and next_data != EMPTY_NODE:
                next_data = second_pointer.next.data
                second_pointer.next.data = second_pointer.data
                second_pointer.data = next_data
                second_pointer = second_pointer.next
            if second_pointer.next is None:
                second_pointer.next = Node(second_pointer.data)
                second_pointer.data = EMPTY_NODE
        else:
            first_pointer = first_pointer.next
