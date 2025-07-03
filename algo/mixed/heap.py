"""
 we need to keep the tree balanced. Using a list to implement the tree
 is a good way of keeping it balanced.
 if parent at p index, then left child is at 2*p and right child at 2*p+1
 heap order property the key at each child is smaller than the one of the
 parent

 Heapsort takes n*log(n). Because build_heap takes n and then there are
  n-1 calls to heapify taking log(n) each.
Therefore, overall we have n+(n-1)log(n)
"""
import numpy as np


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.currentSize = 0

    def buildHeap(self, alist):
        """the brute-force way of building a heap is by using binary search to
        decide where to insert and then insert. However at worst, the value may
        be inserted in the middle and require doing n shifts. So, this would
        require log(n)*n operations.

        If we instead start from the middle, at the lowest parent
        and percolate down we can build the whole heap with n operations
        (log(n)*n/2).

        https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        """
        mid_idx = len(alist) // 2  # we start from the lowest parent
        self.currentSize = len(alist)
        # [0] is used to make indexes +1 and easier to reason about
        self.heap_list = [0] + alist[:]
        while mid_idx > 0:
            self._percolate_down(mid_idx)
            mid_idx -= 1

    def insert(self, k):
        """Insert at the end and percolate up"""
        self.heap_list.append(k)
        self.currentSize = self.currentSize + 1
        self._percolate_up(self.currentSize)

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = (
                    self.heap_list[i // 2],
                    self.heap_list[i],
                )
            i = i // 2

    def delete_min(self):
        retval, self.heap_list[1] = (
            self.heap_list[1],
            self.heap_list[self.currentSize],
        )
        self.currentSize -= 1
        self.heap_list.pop()
        self._percolate_down(1)
        return retval

    def _percolate_down(self, i):
        while (i * 2) <= self.currentSize:
            min_child = self.smallest_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = (
                    self.heap_list[mc],
                    self.heap_list[i],
                )
            i = min_child

    def smallest_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


class Bar:
    def __init__(self, doa: str):
        self._doa = doa


class Foo:
    def __init__(self, bar: Bar) -> None:
        self._bar = bar

    def test(self, val1: int, val2: str) -> str:
        """This is a test docstring
        It takes as args:
            val1: int
            val2: str
        """
        val3 = val1**2
        return str(val3) + val2


fii = Foo(bar=Bar(doa="bar"))

fii.test(val1=10, val2="bar")

fii.test(val1=3, val2="foo")

np.array([1, 2])

