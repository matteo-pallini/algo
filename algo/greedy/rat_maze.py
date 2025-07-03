def run_maze(maze):
    backtrack = [[False for _ in row] for row in maze]
    next_move(maze, 0, 0, backtrack)
    return backtrack


def next_move(maze, x, y, backtrack):
    if (x == len(maze) - 1) and (y == len(maze[0]) - 1):
        return True
    for new_x, new_y in [(x + 1, y), (x, y + 1)]:
        if ((new_x < len(maze[0]))
                and (new_y < len(maze))
                and (maze[new_x][new_y] == 1)
                and (not backtrack[new_x][new_y])
        ):
            backtrack[new_x][new_y] = True
            reached_end = next_move(maze, new_x, new_y, backtrack)
            if reached_end:
                return True
            else:
                backtrack[new_x][new_y] = False