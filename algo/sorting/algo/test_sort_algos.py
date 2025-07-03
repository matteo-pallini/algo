import copy
import unittest
from sorting.algo import insert_sort, radix_sort, Heap

import functools

from sorting.algo.merge_sort_2nd import merge_sort
from sorting.algo.quick_sort_2nd import quicksort


class BaseTest(unittest.TestCase):
    basic_cases = [
        [0, 41, -21, 11, 3, 8, 37],
        [-21, 0, 3, 8, 11, 37, 41],
        [41, 37, 11, 8, 3, 0, -21],
    ]

    expected = [-21, 0, 3, 8, 11, 37, 41]

    def run_sorting_algo_on_array(self, sorting_algo):
        for case in self.basic_cases:
            sorting_algo(case)
            self.assertListEqual(case, self.expected)

    def test_insert_sort(self):
        self.run_sorting_algo_on_array(insert_sort)

    def test_merge_sort(self):
        self.run_sorting_algo_on_array(functools.partial(
            merge_sort, start=0, end=len(self.basic_cases[0])))

    # def test_radix_sort(self):
    #     self.run_sorting_algo_on_array(radix_sort)

    def test_quicksort(self):
        for case in self.basic_cases:
            case_copy = copy.copy(case)
            quicksort(case_copy, start=0, end=len(case)-1)
            self.assertListEqual(case_copy, self.expected)


class TestHeap(unittest.TestCase):
    basic_case = [2, 1, 3, 0]

    def test_max_heapify(self):
        heap = Heap(self.basic_case, max_heap=True)
        heap.build_heap()
        self.assertEqual(heap.array[0], 3)

    def test_min_heapify(self):
        heap = Heap(self.basic_case, max_heap=False)
        heap.build_heap()
        self.assertEqual(heap.array[0], 0)

    def test_heap_sort(self):
        basic_cases = [
            [0, 4, 2, 1, 3],
            [0, 1, 2, 3, 4],
            [4, 3, 2, 1, 0],
        ]

        expected = [0, 1, 2, 3, 4]

        for case in basic_cases:
            heap = Heap(case, max_heap=True)
            heap.heap_sort()
            self.assertListEqual(heap.array, expected)

    def test_heap_extract_head(self):
        array = [0, 4, 2, 1, 3]
        heap = Heap(array, max_heap=True)
        heap.build_heap()
        head = heap.extract_head()
        self.assertEqual(head, 4)
        self.assertEqual(heap.heap_size, len(array) - 1)

    def test_increase_val(self):
        array = [0, 4, 2, 1, 3]
        heap = Heap(array, max_heap=True)
        heap.build_heap()
        heap.increase_val(3, 5)
        self.assertEqual(heap.array, [5, 4, 2, 3, 0])

    def test_insert_val(self):
        array = [0, 4, 2, 1, 3]
        heap = Heap(array, max_heap=True)
        heap.build_heap()
        heap.max_heap_insert_key(5)
        self.assertEqual(heap.array, [5, 3, 4, 1, 0, 2])
        self.assertEqual(heap.heap_size, 6)
