import abc
import dataclasses
from typing import Iterable, TypeVar, Callable, Sequence

T = TypeVar("T")

@dataclasses.dataclass
class Comparator:
    good: bool

    @abc.abstractmethod
    def __call__(self, v0: T, v1: T) -> bool:
        raise NotImplementedError

@dataclasses.dataclass
class Or:
    comparators: Sequence[Comparator]
    good: bool = True

    def __call__(self, v0: T, v1: T) -> bool:
        comparators_res = [e(v0, v1) for e in self.comparators]
        self.good = self.good and any(comparators_res)
        return self.good

@dataclasses.dataclass
class Increasing(Comparator):
    def __call__(self, v0: int, v1: int) -> bool:
        self.good = self.good and v0 <= v1
        return self.good

@dataclasses.dataclass
class Decreasing(Comparator):
    def __call__(self, v0: int, v1: int) -> bool:
        self.good = self.good and v0 >= v1
        return self.good


@dataclasses.dataclass
class Range(Comparator):
    min_val: int
    max_val: int

    def __call__(self, v0: int, v1: int) -> bool:
        self.good = self.good and self.min_val <= abs(v0 - v1) <= self.max_val
        return self.good

@dataclasses.dataclass
class LineAdjacentValues:
    vals: list[int]
    def is_safe(self, comparators: Iterable[Comparator]) -> bool:
        for c in comparators:
            for idx, v in enumerate(self.vals[:-1]):
                if not c(v, self.vals[idx+1]):
                    return False
        return True


if __name__ == "__main__":
    with open("./vals.txt", "rt") as handle:
        safe_list = []
        for l in handle.readlines():
            comparators = [
                Or(comparators=[Increasing(True), Decreasing(True)]),
                Range(min_val=1, max_val=3, good=True)
            ]
            safe = LineAdjacentValues(vals=[int(e) for e in l.split(" ")]).is_safe(comparators)
            safe_list.append(safe)
        print(sum(safe_list))

