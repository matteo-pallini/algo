import unittest

from linked_lists.LinkedList_2nd_take import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_multiple_insert(self):
        ll = LinkedList()
        ll.insert(5)
        ll.insert(10)
        ll.insert(11)
        self.assertEqual(ll.head.value, 11)
        # self.assertEqual(ll.tail.value, 5)

    def test_search(self):
        ll = LinkedList()
        ll.insert(5)
        ll.insert(10)
        ll.insert(11)
        search_result = ll.search_node(5)
        self.assertEqual(search_result.value, 5)
        self.assertEqual(search_result.next, None)

    def test_delete(self):
        ll = LinkedList()
        ll.insert(5)
        ll.insert(10)
        ll.insert(11)
        ll.delete_node(10)
        search_result = ll.search_node(5)
        self.assertEqual(search_result.prev.value, 11)
        self.assertEqual(search_result.next, None)

    def test_head_tail(self):
        ll = LinkedList()
        ll.insert(5)
        ll.insert(10)
        ll.insert(11)
        self.assertEqual(ll.head.value, 11)
        # self.assertEqual(ll.tail.value, 5)