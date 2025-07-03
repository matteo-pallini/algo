def num_enclave(grid):
    visited = set()
    stack = []
    cols, rows = len(grid[0]), len(grid)
    stack.extend([e for r in range(rows) for e in [(r, 0), (r, cols-1)]])
    stack.extend([e for c in range(1, cols) for e in [(0, c), (rows-1, c)]])
    while stack:
        elem = stack.pop()
        if elem in visited:
            continue
        visited.add(elem)
        if grid[elem[0]][elem[1]] == 0:
            continue
        for (v, h) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_coord = (elem[0]+v, elem[1]+h)
            if (new_coord in visited
                or new_coord[0] < 0
                or new_coord[0] > rows-1
                or new_coord[1] < 0
                    or new_coord[1] > cols-1):
                continue
            else:
                if grid[new_coord[0]][new_coord[1]] == 1:
                    stack.append(new_coord)
                else:
                    visited.add(new_coord)
    remote = 0
    for row_idx in range(rows):
        for col_idx in range(cols):
            if (row_idx, col_idx) not in visited and grid[row_idx][col_idx] == 1:
                remote += 1
    return remote
