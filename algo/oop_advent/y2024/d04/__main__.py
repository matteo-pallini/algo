import copy
from typing import NamedTuple

Matrix = list[list[str]]

class Point(NamedTuple):
    x: int
    y: int

def check_one(point:Point, shift_x:int, shift_y:int, matrix: Matrix, letters: list[str]) -> bool:
    width = len(matrix[0]) if matrix else 0
    length = len(matrix if matrix else 0)
    new_point = Point(x=point.x + shift_x, y=point.y + shift_y)
    if 0 <= new_point.x < width and 0 <= new_point.y < length and matrix[new_point.y][new_point.x] == letters[0]:
        return True
    return False


def search(matrix: Matrix, letters: list[str], options: [list[Point]]) -> list[Point]:
    matches = []
    for idx_y, x_array in enumerate(matrix):
        for idx_x, value in enumerate(x_array):
            point = Point(x=idx_x, y=idx_y)
            if matrix[point.y][point.x] == letters[0]:
                for (s_x, s_y) in options:
                    s_x_copy, s_y_copy, letters_copy = copy.copy(s_x), copy.copy(s_y), copy.copy(letters[1:])
                    while letters_copy:
                        if check_one(point, shift_x=s_x_copy, shift_y=s_y_copy, matrix=matrix, letters=letters_copy):
                            s_x_copy, s_y_copy = s_x_copy + s_x, s_y_copy + s_y
                            letters_copy = letters_copy[1:]
                        else:
                            break
                    if len(letters_copy) == 0:
                        matches.append(point)
    return matches


def search_x_pattern(matrix: Matrix, letters: list[str]):
    final_matches = []
    first_axis, second_axis = [Point(1, 1)], [Point(-1, 1)]
    matches_first_axis = set(search(matrix,letters, first_axis))
    matches_first_axis_reverse = search(matrix, letters[::-1], first_axis)
    matches_first_axis_final = matches_first_axis.union(matches_first_axis_reverse)
    matches_second_axis = set(search(matrix, letters, second_axis))
    matches_second_axis_reverse = search(matrix, letters[::-1], second_axis)
    matches_second_axis_final = matches_second_axis.union(matches_second_axis_reverse)
    expected_shift = len(letters) - 1
    # print(sorted(matches_first_axis, key=lambda x: (x.y, x.x)), "\t\t", sorted(matches_first_axis_reverse, key=lambda x: (x.y, x.x)))
    # print(sorted(matches_second_axis, key=lambda x: (x.y, x.x)), "\t\t", sorted(matches_second_axis_reverse, key=lambda x: (x.y, x.x)))
    for point in matches_first_axis_final:
        if Point(x=point.x + expected_shift, y=point.y) in matches_second_axis_final:
            final_matches.append(point)
    return final_matches


if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        matrix: Matrix = [[letter for letter in line] for line in handle.read().splitlines() ]
        first_options = [Point(0,1), Point(0,-1), Point(1,0), Point(-1,0), Point(-1, -1), Point(1, -1), Point(1, 1), Point(-1, 1)]
        matches = search(matrix, ["X", "M", "A", "S"], first_options)
        print(len(matches))
        assert len(matches) == 2530 or len(matches) == 18
        matches_second_part = search_x_pattern(matrix, ["M", "A", "S"])
        print(len(matches_second_part))



