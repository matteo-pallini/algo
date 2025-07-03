9: 40


0 - 1 - 1 - 1
| | |
1 - 2 - 3 - 4
| | |
1 - 3 - 6 - 10
|
1 - 4 - 10 - 20


def number_of_ways_fct(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left
        return number_of_ways[x][y]
    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n-1, m-1)


def number_of_ways_space_fct(n, m):
    min_v, max_v = min(n, m), max(n, m)
    vals = [1] * min_v
    for _ in range(max_v-1):
        for idx in range(min_v):
            if idx == 0:
                vals[idx] = vals[idx]
            else:
                vals[idx] += vals[idx-1]
    return vals[-1]
