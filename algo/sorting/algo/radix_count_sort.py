"""
In a nutshell you want to count how many elements there are with value below x and position x accordingly. So, if there
are 15 elements below x, this should take the 16th position
- count sort is a stable sort
- it is not a comparison-sort, ie the sorting logic does not rely on comparing values between each other
- it sorts in linear time o(n+k), where k is the max value in the input_array.
- running counting sort takes o(k) extra memory besides the one taken by input_array
- Counting sort is efficient if the range of input data is not significantly greater than the number of objects
to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
here the k component in the time complexity is much more relevant than the n one.
- counting sort is stable. Numbers with the same value appear in the output array in the same order as they do in the
input array. Ties between two numbers are solved preserving the order in the input array.
- Radix sort requires a stable sorting algo, we need to keep numbers with the same digit for a decimal
in the original order, otherwise the ordering of lower decimals will be broken by higher ones.  eg [12, 13] when sorting
by the 2nd decimal we need to keep the 2 and 3 as they are, otherwise they may end up being [13, 12].
"""
import math
import functools


def counting_sort(input_array, output_array, get_index=None):
    if get_index:
        min_val = -min(input_array) if min(input_array) < 0 else 0
        input_array_decimal = [get_index(e + min_val) for e in input_array]
    else:
        input_array_decimal = input_array
    base_array = [0] * 10

    for v in input_array_decimal:
        base_array[v] += 1

    for i in range(1, len(base_array)):
        base_array[i] += base_array[i - 1]

    for idx in range(len(input_array))[::-1]:
        output_array[base_array[input_array_decimal[idx]] - 1] = input_array[idx]
        base_array[input_array_decimal[idx]] -= 1


def radix_sort(input_array):
    output_array = [None] * len(input_array)
    digits = int(math.log10(max(input_array))) + 1
    for d in range(digits):
        counting_sort(input_array, output_array, functools.partial(get_digit, d=d + 1))
    return output_array


def get_digit(n, d):
    for i in range(d - 1):
        n //= 10
    return n % 10
