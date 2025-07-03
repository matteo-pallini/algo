def happy_string_k(n, k):
    letters = ["a", "b", "c"]
    n_combinations = 3 * 2 ** (n-1)
    if k > n_combinations:
        return ""

    space = n_combinations//3
    idx = (k-1)//space
    last = letters[idx]
    final = [last]

    value = k - 1 - idx * space
    while value >= 0 and n > 1:
        half_space = space//2
        idx = value//half_space
        last = [e for e in letters if e != last][idx]
        value = value - idx * half_space
        space = half_space
        final.append(last)
        if half_space == 1:
            break
    return "".join(final)
