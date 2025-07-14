import abc
from collections import Counter
from typing import Generic, TypeVar, Generator, Iterable

T = TypeVar("T")



class Combiner(abc.ABC, Generic[T]):

    def __init__(self, sequence1: Iterable[T], sequence2: Iterable[T]):
        self._seq1 = sequence1
        self._seq2 = sequence2

    @abc.abstractmethod
    def combine(self) -> Iterable[T]:
        raise NotImplementedError


class DifferenceCombiner(Combiner):

    def combine(self) -> Generator[T, None, None]:
        for a1, a2 in zip(self._seq1, self._seq2):
            yield abs(a1 - a2)


class FrequencyCombiner(Combiner):

    def combine(self) -> Generator[T, None, None]:
        counter = Counter(self._seq2)
        for a1 in self._seq1:
            yield counter.get(a1, 0)


class MultiplicativeCombiner(Combiner):

    def combine(self) -> Generator[T, None, None]:
        for a1, a2 in zip(self._seq1, self._seq2):
            yield a1 * a2


if __name__ == "__main__":
    vals1, vals2 = [], []
    with open("./location_ids.txt", "rt") as handle:
        for l in handle.readlines():
            v1, v2 = l.replace("\n", "").split("   ")
            vals1.append(int(v1))
            vals2.append(int(v2))
    print(sum(DifferenceCombiner(sorted(vals2), sorted(vals1)).combine()))

    print(sum(MultiplicativeCombiner(vals1, FrequencyCombiner(vals1, vals2).combine()).combine()))
