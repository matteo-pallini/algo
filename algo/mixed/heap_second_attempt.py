from typing import Callable, Optional


class Heap:

    def __init__(self, comparator: Callable[[int, int], bool], array: Optional[list[int]] = None):
        array = array if array else []
        self.length = len(array)
        self.array: list[Optional[int]] = [None] + array  # used None here to make the math for identifying children and parents easier
        self._comparator = comparator
        self.heapify()


    def heapify(self):
        mid = self.length // 2
        while mid > 0:
            self._bubble_down(mid)
            mid -= 1

    def remove_head(self) -> Optional[int]:
        if self.length >= 1:
            head = self.array[1]
            self.array[1] = self.array[-1]
            self.array.pop()
            self.length -= 1
            self._bubble_down(1)
            return head

    def insert(self, value: int) -> None:
        self.array.append(value)
        self.length += 1
        self._bubble_up(self.length)

    def _bubble_down(self, idx: int) -> None:
        next_head, left_child, right_child = idx, idx*2, idx*2+1
        if left_child <= self.length and self._comparator(self.array[left_child], self.array[idx]):
            next_head = left_child
        if right_child <= self.length and self._comparator(self.array[right_child], self.array[next_head]):
            next_head = right_child
        if next_head != idx:
            self.array[next_head], self.array[idx] = self.array[idx], self.array[next_head]
            self._bubble_down(next_head)

    def _bubble_up(self, idx: int) -> None:
        parent = idx // 2
        if parent > 0:
            if self._comparator(self.array[idx], self.array[parent]):
                self.array[parent], self.array[idx] = self.array[idx], self.array[parent]
                self._bubble_up(parent)


if __name__ == "__main__":
    import operator
    max_heap = Heap(operator.gt, [3, 1, 7, 9, 2, 5])
    expected = [9, 7, 5]
    for e in expected:
        assert max_heap.remove_head() == e
    max_heap.insert(11)
    max_heap.insert(4)
    expected = [11, 4, 3, 2, 1]
    for e in expected:
        assert max_heap.remove_head() == e
