import unittest

from linked_lists.LinkedList import LinkedList
from linked_lists.exercises.partition import partition
from linked_lists.exercises.remove_dups import remove_duplicates
from linked_lists.exercises.return_k_to_last import return_k_to_last
from linked_lists.exercises.merge_two_sorted import Node, merge_two_sorted


def prepare_linked_list(values):
    node = Node(data=values[0])
    start = node
    for v in values[1:]:
        node.next = Node(data=v)
        node = node.next
    return start


def get_values_from_linked_list(linked_list):
    values = []
    while linked_list:
        values.append(linked_list.data)
        linked_list = linked_list.next
    return values


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList(1)
        self.ll.add_element(2)
        self.ll.add_element(3)

    def test_adding_element(self):
        self.assertEqual(self.ll.head.next.data, 2)

    def test_deleting_element(self):
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 3)
        self.assertEqual(self.ll.head.next.prev.data, 1)

        self.ll.head.next.delete_node()

        self.assertEqual(self.ll.head.next.data, 3)
        self.assertEqual(self.ll.head.next.prev.data, 1)
        self.assertIsNone(self.ll.head.next.next)

    def test_get_size(self):
        self.assertEqual(self.ll.get_size(), 3)
        self.ll.head.next.delete_node()
        self.assertEqual(self.ll.get_size(), 2)

    def test_get_values(self):
        values = self.ll.get_values()
        expected = [1, 2, 3]
        self.assertEqual(values, expected)


class TestRemoveDups(unittest.TestCase):

    def test_base_dups_removal(self):
        values = [1, 2, 2, 3, 4, 5, 1, 4, 3]
        ll = LinkedList(values[0])
        for v in values[1:]:
            ll.add_element(v)

        self.assertEqual(ll.get_size(), len(values))
        ll_no_dups = remove_duplicates(ll)
        node = ll_no_dups.head
        while node.next:
            node = node.next
        self.assertEqual(ll_no_dups.get_size(), len(set(values)))

        self.assertEqual(ll_no_dups.get_values(), sorted(list(set(values))))


class TestReturnKToLast(unittest.TestCase):

    def test_return_k_to_last(self):
        values = [1, 2, 2, 3, 4, 5, 1, 4, 3]
        ll = LinkedList(values[0])
        for v in values[1:]:
            ll.add_element(v)

        actual = return_k_to_last(ll, 2)
        self.assertEqual(actual.data, 1)

        actual = return_k_to_last(ll, 1)
        self.assertEqual(actual.data, 4)

        actual = return_k_to_last(ll, 4)
        self.assertEqual(actual.data, 4)


class TestPartition(unittest.TestCase):

    def test_partition_base_case(self):
        values = [7, 3, 1, 2, 8, 4, 3]
        cutoff = 4
        ll = LinkedList(values[0])
        for v in values[1:]:
            ll.add_element(v)

        partition(ll, cutoff)
        actual = ll.get_values()
        expected = [3, 1, 2, 3, " ", 4, 8, 7]
        self.assertEqual(actual, expected)

    def test_partition_small_case(self):
        values = [3, 8]
        cutoff = 4
        ll = LinkedList(values[0])
        for v in values[1:]:
            ll.add_element(v)

        partition(ll, cutoff)
        actual = ll.get_values()
        expected = [3, " ", 8]
        self.assertEqual(actual, expected)

    def test_partition_all_below_butoff(self):
        values = [3, 2, 1]
        cutoff = 4
        ll = LinkedList(values[0])
        for v in values[1:]:
            ll.add_element(v)

        partition(ll, cutoff)
        actual = ll.get_values()
        expected = [3, 2, 1]
        self.assertEqual(actual, expected)


class TestMergeTwoSorted(unittest.TestCase):

    def test_base_case(self):
        first = prepare_linked_list([1, 3, 4, 7, 12])
        second = prepare_linked_list([1, 2, 3, 14])

        final = merge_two_sorted(first, second)
        expected = prepare_linked_list([1, 1, 2, 3, 3, 4, 7, 12, 14])
        self.assertListEqual(
            get_values_from_linked_list(final),
            get_values_from_linked_list(expected),
        )

    def test_two_sequences(self):
        first = prepare_linked_list([1, 2, 4])
        second = prepare_linked_list([14])
        final = merge_two_sorted(first, second)
        expected = prepare_linked_list([1, 2, 4, 14])
        self.assertListEqual(
            get_values_from_linked_list(final),
            get_values_from_linked_list(expected),
        )

    def test_equals(self):
        first = prepare_linked_list([2, 2])
        second = prepare_linked_list([2])
        final = merge_two_sorted(first, second)
        expected = prepare_linked_list([2, 2, 2])
        self.assertListEqual(
            get_values_from_linked_list(final),
            get_values_from_linked_list(expected),
        )
