import copy
import dataclasses
from collections import defaultdict
from typing import DefaultDict, Tuple


@dataclasses.dataclass
class Node:
    value: str
    met: bool = False

@dataclasses.dataclass
class UpdatesChecker:
    _tree : DefaultDict[str, DefaultDict[str, Node]] = dataclasses.field(default_factory=lambda: defaultdict(defaultdict))
    _encountered: DefaultDict[str, Node] = dataclasses.field(default_factory=lambda: defaultdict(Node))

    def add_rule(self, rule: str):
        first, second = rule.split("|")
        if second not in self._encountered:
            self._encountered[second] = Node(second)
        self._tree[first][second] = self._encountered[second]

    def check_row(self, row: list[str]) -> bool:
        for v in self._encountered.values():
            v.met = False
        for r in row:
            #print(r, self._tree[r].values(), self._encountered)
            for node in self._tree[r].values():
                if node.met:
                    return False
            if r not in self._encountered:
                self._encountered[r] = Node(value=r, met=True)
            self._encountered[r].met = True
        return True

    def sort_row(self, row: list[str]) -> list[str]:
        new_row = copy.copy(row)
        idx = 1
        while idx < len(new_row):
            if idx == 0:
                idx += 1
                continue
            if new_row[idx-1] in self._tree[new_row[idx]]:
                new_row[idx-1], new_row[idx] = new_row[idx], new_row[idx-1]
                idx -= 1
            else:
                idx += 1
        return new_row

    def new(self) -> "UpdatesChecker":
        new_checker = copy.deepcopy(self)
        for v in new_checker._encountered.values():
            v.met = False
        return new_checker


def split_rows(updates_checker_master: UpdatesChecker, rows: list[list[str]]) -> Tuple[list[list[str]], list[list[str]]]:
    good_rows, bad_rows = [], []
    for r in rows:
        updates_checker = updates_checker_master.new()
        if updates_checker.check_row(r):
            good_rows.append(r)
        else:
            bad_rows.append(r)
    return good_rows, bad_rows


def compute_final_count(rows: list[list[str]]) -> int:
    final = 0
    for row in rows:
        mid = len(row) // 2
        final += int(row[mid])
    return final


if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        rows = []
        updates_checker_master, completed_rules = UpdatesChecker(), False
        for line in handle.read().splitlines():
            if completed_rules:
                rows.append(line.split(","))
            elif line == "":
                completed_rules = True
            else:
                updates_checker_master.add_rule(line)

        good_rows, bad_rows = split_rows(updates_checker_master=updates_checker_master, rows=rows)
        sorted_bad = []
        for b in bad_rows:
            sorted_bad.append(updates_checker_master.sort_row(b))
        final = compute_final_count(good_rows)
        final_bad = compute_final_count(sorted_bad)
        print(final, final_bad)





