
def delete_duplicates(arr):
    i = 0
    for _ in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            del arr[i+1]
        else:
            i += 1
    return arr