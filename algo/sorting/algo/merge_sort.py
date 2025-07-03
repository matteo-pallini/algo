"""
Divide-conquer-combine approach
- Does not operate in place, it is memory expensive
- worst time complexity of n*log(n). Intuition behind complexity: Given the binary split for each merge_sort we end up
having log(n-1) steps, each one requiring n operations for the merge step + the base level (containing 1 value per leaf).
So, we have n * log(n) steps at worst
- stable sort. Stable sorts are necessary when using sorting approaches like radix sort and to be preferred if
- usually used with Linked List, quicksort can't be used with random pivot as efficiently as with arrays, so quicksort would
be less efficient.
- with Linked List we can insert items anywhere with o(1) time, if we have a pointer to the previous node.
"""

import math


def merge_sort(array, start, end):
    if (end - start) > 1:
        slice_point = int((end + start) / 2)
        merge_sort(array, start, slice_point)
        merge_sort(array, slice_point, end)
        merge(array, start, slice_point, end)


def merge(array, start, slice_point, end):
    slice_1 = array[start: slice_point]
    slice_2 = array[slice_point: end + 1]
    slice_1.append(math.inf)
    slice_2.append(math.inf)
    pointer_1 = 0
    pointer_2 = 0

    for i in range(start, end):
        if slice_1[pointer_1] < slice_2[pointer_2]:
            array[i] = slice_1[pointer_1]
            pointer_1 += 1
        else:
            array[i] = slice_2[pointer_2]
            pointer_2 += 1
