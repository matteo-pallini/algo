"""
- sort in place
- time complexity at worst n^2 if sorted in reverse. Coming from n(n-1)/2, for each value minus the first we loop through
each other vaule and shift it if necessary. We basically re-shift the whole array for each j, if necessary
"""


def insert_sort(array):
    for j in range(1, len(array)):
        k = array[j]
        i = j - 1
        while i >= 0 and array[i] > k:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = k
