

def insert_sort(array):

    for j in range(1, len(array)):
        i = j - 1
        k = array[j]
        while i >= 0 and array[i] > k:
            array[i+1], array[i] = array[i], array[i+1]
            i -= 1
        array[i+1] = k