import copy
import dataclasses
from collections import defaultdict
from typing import DefaultDict

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

    def check_row(self, row: [str]) -> bool:
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

    def new(self) -> "UpdatesChecker":
        new_checker = copy.deepcopy(self)
        for v in new_checker._encountered.values():
            v.met = False
        return new_checker


def get_good_rows(updates_checker_master: UpdatesChecker, rows: list[list[str]]) -> list[list[str]]:
    good_rows = []
    for r in rows:
        updates_checker = updates_checker_master.new()
        if updates_checker.check_row(r):
            good_rows.append(r)
    return good_rows


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

        good_rows = get_good_rows(updates_checker_master=updates_checker_master, rows=rows)
        final = compute_final_count(good_rows)
        print(final)





