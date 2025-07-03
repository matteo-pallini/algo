
def palindromicity(string_):
    string_lower = string_.lower()
    lower_idx = 0
    upper_idx = -1
    while lower_idx + 1 <= len(string_lower) + upper_idx:
        while not string_lower[lower_idx].isalnum():
            lower_idx += 1
        while not string_lower[upper_idx].isalnum():
            upper_idx -= 1
        if string_lower[lower_idx] != string_lower[upper_idx]:
            return False

        lower_idx += 1
        upper_idx -= 1
    return True
