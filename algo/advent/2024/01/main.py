from typing import Generic, TypeVar, Generator

T = TypeVar("T")

class LocationList(Generic[T]):
    def __init__(self, vals: list[T]):
        self._vals = self._initialise(vals)

    def _initialise(self, vals: list[T]) -> list[T]:
        return sorted(vals)

    def __next__(self) -> Generator[T, None, None]:
        yield from self._vals

    def __iter__(self):
        return iter(self._vals)


def get_diffs(list1: LocationList[T], list2: LocationList[T]) -> list[T]:
    vals: list[T] = []
    for a1, a2 in zip(list1, list2):
        vals.append(abs(a1 - a2))
    return vals


if __name__ == "__main__":
    vals1, vals2 = [], []
    with open("./location_ids.txt", "rt") as handle:
        for l in handle.readlines():
            v1, v2 = l.replace("\n", "").split("   ")
            vals1.append(int(v1))
            vals2.append(int(v2))
    print(sum(get_diffs(LocationList(vals2), LocationList(vals1))))
