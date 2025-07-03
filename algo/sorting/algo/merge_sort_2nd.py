import math


def merge_sort(array, start, end):
    if (end - start) > 1:
        midpoint = (start + end) // 2
        merge_sort(array, start, midpoint)
        merge_sort(array, midpoint, midpoint)
        merge(array, start, midpoint, end)


def merge(array, start, midpoint, end):
    slice_1, slice_2 = array[start:midpoint], array[midpoint:end+1]
    pointer_1, pointer_2 = 0, 0
    slice_1.append(math.inf)
    slice_2.append(math.inf)

    for idx in range(start, end):
        if slice_1[pointer_1] < slice_2[pointer_2]:
            array[idx] = slice_1[pointer_1]
            pointer_1 += 1
        else:
            array[idx] = slice_2[pointer_2]
            pointer_2 += 1
