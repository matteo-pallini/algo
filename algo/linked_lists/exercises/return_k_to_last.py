from typing import Union

from linked_lists.LinkedList import LinkedList, Node


def return_k_to_last(linked_list: Union[LinkedList, Node], k: int):

    def recursive_function(linked_list: Union[LinkedList, Node], k: int):
        node = getattr(linked_list, 'head', linked_list)
        if node is None:
            return None
        else:
            recursed_node = recursive_function(node.next, k)
            counter[0] += 1
            if counter[0] == k:
                return node
            else:
                return recursed_node

    counter = [-1]
    return recursive_function(linked_list, k)
