
def advance(arr, start, next_step):
    if start + next_step >= len(arr) - 1:
        return True
    else:
        next_value = arr[start + next_step]

        if next_value > 0:
            for i in reversed(range(1, next_value + 1)):
                outcome = advance(arr, start + next_step, i)
                if outcome:
                    return True

    return False
