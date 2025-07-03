import unittest

from trees.binary_search_tree import BSTree
from trees.tree import Tree
from trees.trie import Trie
from trees.utils import inorder_traversal, preorder_traversal, postorder_traversal


class TestTraversals(unittest.TestCase):

    tree = BSTree()
    for value in [10, 9, 11, 14, 18, 12, 7]:
        tree.insert_value(value)

    external_tree = Tree()
    for value in range(1, 6):
        external_tree.insert_value(value)

    def test_inorder_traversal(self):
        traversed_tree = inorder_traversal(self.tree.root)
        self.assertListEqual(traversed_tree, [7, 9, 10, 11, 12, 14, 18])

    def test_external_tree_inorder_traversal(self):
        traversed_tree = inorder_traversal(self.external_tree.root)
        self.assertListEqual(traversed_tree, [4, 2, 5, 1, 3])

    def test_preorder_traversal(self):
        traversed_tree = preorder_traversal(self.tree.root)
        self.assertListEqual(traversed_tree, [10, 9, 7, 11, 14, 12, 18])

    def test_external_tree_preorder_traversal(self):
        traversed_tree = preorder_traversal(self.external_tree.root)
        self.assertListEqual(traversed_tree, [1, 2, 4, 5, 3])

    def test_postorder_traversal(self):
        traversed_tree = postorder_traversal(self.tree.root)
        self.assertListEqual(traversed_tree, [7, 9, 12, 18, 14, 11, 10])

    def test_external_tree_postorder_traversal(self):
        traversed_tree = postorder_traversal(self.external_tree.root)
        self.assertListEqual(traversed_tree, [4, 5, 2, 3, 1])


class TestTrie(unittest.TestCase):

    def test_insert_one(self):
        foo = Trie()
        foo.insert("doggy")
        foo.insert("cat")
        self.assertTrue("*" in foo._main_dict["d"]["o"]["g"]["g"]["y"])
        self.assertTrue("*" in foo._main_dict["c"]["a"]["t"])
        self.assertFalse("*" in foo._main_dict["c"]["a"])

    def test_insert_many(self):
        foo = Trie()
        foo.insert_many(["doggy", "cat", "foo"])
        self.assertTrue("*" in foo._main_dict["d"]["o"]["g"]["g"]["y"])
        self.assertTrue("*" in foo._main_dict["c"]["a"]["t"])
        self.assertFalse("*" in foo._main_dict["c"]["a"])

    def test_search(self):
        foo = Trie()
        foo.insert_many(["doggy", "cat", "foo"])
        self.assertTrue(foo.search("doggy"))
        self.assertFalse(foo.search("catty"))
