class MaxHeap:

    def __init__(self, array):
        self.length = len(array)
        self._array = [0]+array

    def heapify(self):
        idx = self.length//2
        while idx > 0:
            self._percolate_down(idx)
            idx -= 1

    def insert(self, value):
        self._array.append(value)
        self.length += 1
        self.percolate_up(self.length)

    def delete_max(self):
        self.length -= 1
        self._array[1] = self._array[-1]
        self._array.pop()
        self._percolate_down(1)

    def _percolate_up(self, idx):
        while idx // 2 > 0:
            if self._array[idx] > self._array[idx//2]:
                self._array[idx //
                            2], self._array[idx] = self._array[idx], self.array[idx//2]

    def _percolate_down(self, idx):
        while idx*2 <= self.length:
            min_child = self.get_min_child(idx)
            if self._array[idx] < self._array[min_child]:
                self._array[idx], self._array[min_child] = self._array[min_child], self._array[idx]
            idx = min_

    def get_min_child(self, idx):
        if idx*2+1 > self.length:
            return idx*2
        else:
            if self.array[idx*2] > self.array[idx*2+1]:
                return idx*2
            else:
                return idx*2+1
