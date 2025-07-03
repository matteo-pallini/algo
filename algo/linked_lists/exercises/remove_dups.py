from linked_lists.LinkedList import LinkedList


def remove_duplicates(linked_list: LinkedList):
    first_pointer = linked_list.head
    while first_pointer.next is not None:
        data = first_pointer.data
        second_pointer = first_pointer
        while second_pointer.next is not None:
            if second_pointer.next.data == data:
                second_pointer.next.delete_node()
            else:
                second_pointer = second_pointer.next
        first_pointer = first_pointer.next
    return linked_list
