"""
- Heapsort takes n*log(n). Because build_heap takes n and then there are n-1 calls to heapify taking log(n) each.
Therefore, overall we have n+(n-1)log(n)
"""
import math
import operator


class Heap:

    def __init__(self, array, max_heap=True):
        self.array = array
        self.heap_size = 0
        self.max_heap = max_heap
        self._heap_operator = operator.gt if self.max_heap else operator.lt

    def build_heap(self):
        self.heap_size = len(self.array)
        for i in range(math.ceil(len(self.array) / 2))[::-1]:
            self.heapify(i)

    def heap_sort(self):
        self.build_heap()
        for i in range(1, len(self.array))[::-1]:
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heap_size -= 1
            self.heapify(0)

    @staticmethod
    def parent(i):
        return int((i + 1) / 2) - 1

    @staticmethod
    def left(i):
        return int(2 * (i + 1)) - 1

    @staticmethod
    def right(i):
        return int(2 * (i + 1) + 1) - 1

    @property
    def array_length(self):
        return len(self.array)

    def heapify(self, i):
        left_idx = self.left(i)
        right_idx = self.right(i)
        if left_idx <= self.heap_size - 1 and self._heap_operator(self.array[left_idx], self.array[i]):
            to_move = left_idx
        else:
            to_move = i
        if right_idx <= self.heap_size - 1 and self._heap_operator(self.array[right_idx], self.array[to_move]):
            to_move = right_idx
        if to_move != i:
            self.array[to_move], self.array[i] = self.array[i], self.array[to_move]
            self.heapify(to_move)

    def extract_head(self):
        if self.heap_size < 1:
            raise Exception("Heap too short")
        head = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.heap_size -= 1
        # should I remove also the record from the array?
        self.heapify(0)
        return head

    def increase_val(self, i, new_val):
        if self.array[i] > new_val:
            raise Exception("new value too small")
        self.array[i] = new_val
        while i > 0 and self.array[self.parent(i)] < self.array[i]:
            self.array[i], self.array[self.parent(
                i)] = self.array[self.parent(i)], self.array[i]
            i = self.parent(i)

    def max_heap_insert_key(self, new_val):
        self.array.append(-math.inf)
        self.heap_size += 1
        self.increase_val(self.heap_size - 1, new_val)
