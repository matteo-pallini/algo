

def search_shift(array, val):
    start, end = 0, len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == val:
            return mid
        if array[start] <= val < array[mid]:
            end = mid - 1
        elif array[mid] < val <= array[end]:
            start = mid + 1
        elif array[start] > array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

if __name__ == "__main__":
    print(search_shift([8,9,1,2, 4, 6], 4))
    print(search_shift([8, 9, 1, 2, 4, 6], 9))