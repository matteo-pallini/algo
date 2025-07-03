import unittest
from leetcode.partition_labels import partition_labels
from leetcode import shortest_path


class TestPartitionLabels(unittest.TestCase):

    def test_base_case(self):
        s = "ababcbacadefegdehijhklij"
        expected = [9, 7, 8]
        self.assertListEqual(expected, partition_labels(s))

    def test_base_case(self):
        s = "eccbbbbdec"
        expected = [10]
        self.assertListEqual(expected, partition_labels(s))


class TestShortestPath(unittest.TestCase):

    def test_base_case(self):
        n, red_edges, blue_edges = 3, [[0, 1], [1, 2]], []
        paths = shortest_path.Solution().shortestAlternatingPaths(n, red_edges, blue_edges)
        self.assertListEqual(paths, [0, 1, -1])
