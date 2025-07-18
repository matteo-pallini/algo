from typing import NamedTuple

Matrix = list[list[str]]

class Point(NamedTuple):
    x: int
    y: int


def unidirectional_search(point:Point, shift_x:int, shift_y:int, matrix: Matrix, letters: list[str]) -> bool:
    if len(letters) == 0:
        return True
    width = len(matrix[0]) if matrix else 0
    length = len(matrix if matrix else 0)
    new_point = Point(x=point.x + shift_x, y=point.y + shift_y)
    if 0 <= new_point.x < width and 0 <= new_point.y < length and matrix[new_point.y][new_point.x] == letters[0]:
        return unidirectional_search(new_point, shift_x, shift_y, matrix, letters[1:])
    return False


def search(matrix: Matrix, letters: list[str]) -> list[Point]:
    matches = []
    for idx_y, x_array in enumerate(matrix):
        for idx_x, value in enumerate(x_array):
            point = Point(x=idx_x, y=idx_y)
            if matrix[point.y][point.x] == letters[0]:
                for (s_x, s_y) in [(0,1), (0,-1), (1,0), (-1,0), (-1, -1), (1, -1), (1, 1), (-1, 1)]:
                    if unidirectional_search(point, shift_x=s_x, shift_y=s_y, matrix=matrix, letters=letters[1:]):
                        matches.append(point)
    return matches



if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        matrix: Matrix = [[letter for letter in line] for line in handle.read().splitlines() ]
        matches = search(matrix, ["X", "M", "A", "S"])
        print(len(matches))