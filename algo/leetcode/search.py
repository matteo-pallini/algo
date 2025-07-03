
def search_val(array, val):
    if len(array) <= 1:
        if array:
            if array[0] == val:
                return True
        return False
    mid = len(array) // 2
    if array[mid] == val:
        return True
    elif array[mid] < val:
        return search_val(array[mid:], val)
    else:
        return search_val(array[:mid], val)


if __name__ == "__main__":
    print(search_val([11, 12, 13], 10))