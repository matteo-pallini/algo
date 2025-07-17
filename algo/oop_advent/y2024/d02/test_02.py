from typing import Sequence

from algo.oop_advent.y2024.d02.__main__ import Increasing, Decreasing, Or, Comparator


def compare_expected_actual(comparator: Comparator, vals: Sequence[int], expected: list[bool]):
    actual = []
    for idx, e in enumerate(vals[:-1]):
        actual.append(comparator(e, vals[idx + 1]))
    assert expected == actual, f"actual: {actual}"


if __name__ == "__main__":
    non_monotonic = [1, 3, 2, 4, 5]
    incr = Increasing(True)
    expected = [True, False, False, False]
    compare_expected_actual(incr, non_monotonic, expected)

    decr = Decreasing(True)
    expected = [False, False, False, False]
    compare_expected_actual(decr, non_monotonic, expected)

    or_comp = Or(good=True, comparators=[Increasing(True), Decreasing(True)])
    expected = [True, False, False, False]
    compare_expected_actual(or_comp, non_monotonic, expected)