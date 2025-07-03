def dutch_partitioning(array, i):
    if len(array) <= 1:
        return None
    array[-1], array[i] = array[i], array[-1]
    pivot = array[-1]
    pointer = 0
    for i in range(len(array) - 1):
        if array[i] < pivot:
            array[i], array[pointer] = array[pointer], array[i]
            pointer += 1
    array[pointer], array[-1] = array[-1], array[pointer]


def dutch_partitioning_replacement(array, i):
    if len(array) <= 1:
        return None
    array[0], array[i] = array[i], array[0]
    left_edge, right_edge = 0, 0
    for idx, val in enumerate(array):
        pivot_val = array[left_edge]
        if val <= pivot_val and left_edge != idx:
            array[left_edge], array[right_edge +
                                    1], to_be_shifted = array[idx], array[left_edge], array[right_edge+1]
            if right_edge+1 < idx:
                array[idx] = to_be_shifted
            right_edge += 1
            if val < pivot_val:
                left_edge += 1
    return array
