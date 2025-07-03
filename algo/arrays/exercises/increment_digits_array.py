

def increment_digits_array(array):

    if not array:
        return array

    i = len(array) - 1
    while True:
        if i < 0:
            array.insert(0, 0)
            i = 0
        array[i] = (array[i] + 1) % 10
        if array[i] != 0:
            return array
        i -= 1