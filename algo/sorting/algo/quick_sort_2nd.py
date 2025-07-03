"""
- algo efficiency depends on how balanced the two partitions are. If very unbalanced (eg already sorted array), then
quicksort has insert sort efficiency, ie n^2. Even fairly unbalanced arrays though make it as efficient as merge sort
(on average), ie n*log(n). I may want to add an intuition for the average performance.
- picking the partitioning value randomly ensures that the splits are balanced enough
- quick sort is an in-place sorting algo, so it is more memory efficient than merge sort. Merge sort uses an extra array
to merge the subarrays. It takes also longer to allocate and de-allocate the extra space
- not a stable sort
- usually better with arrays, we need random access to the data container in order to make the splits balanced. Arrays
elements are stored in contiguous memory locations. While if we use Linked List is not the case and in order to move
to a randomly picked element we need to traverse part of the data structure.
"""

import random


def quicksort(array, start, end):
    if (end - start) > 1:
        pivot = get_pivot(array, start, end)
        quicksort(array, start, pivot)
        quicksort(array, pivot, end)


def get_pivot(array, start, end):
    random_pivot = random.choice(range(start, end))
    array[end], array[random_pivot] = array[random_pivot], array[end]

    pivot_value, pivot_point = array[end], start-1

    for idx in range(start, end-1):
        if array[idx] < pivot_value:
            pivot_point += 1
            array[pivot_point], array[idx] = array[idx], array[pivot_point]
    pivot_point += 1
    array[pivot_point], array[end] = array[end], array[pivot_point]
    return pivot_point
