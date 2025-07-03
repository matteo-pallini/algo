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


def quicksort(array, start, end, random_partition=True):
    if (end - start) > 1:
        q = partition(array, start, end, random_partition)
        quicksort(array, start, q, random_partition)
        quicksort(array, q, end, random_partition)


def partition(array, start, end, random_partition):
    """the idea here is that at the end everything smaller than the partitioning value should be at its left
    and everything larger should be at its right
    """
    if random_partition:
        pivot = random.choice(range(start, end))
        array[end], array[pivot] = array[pivot], array[end]

    x = array[end]
    partitioning_threshold = start - 1
    for pivot in range(start, end - 1):
        if array[pivot] < x:
            partitioning_threshold += 1
            array[partitioning_threshold], array[pivot] = array[pivot], array[partitioning_threshold]
    partitioning_threshold+=1
    array[partitioning_threshold], array[end] = array[end], array[partitioning_threshold]
    return partitioning_threshold
