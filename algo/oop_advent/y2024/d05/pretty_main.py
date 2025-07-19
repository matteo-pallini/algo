import dataclasses


@dataclasses.dataclass
class Node:
    value: str
    after: set[str] = dataclasses.field(default_factory=lambda: set())

    def __lt__(self, other: "Node"):
        return other.value in self.after

    def __eq__(self, other):
        return other.value == self.value


@dataclasses.dataclass
class NodesRegistry:
    _registry: dict[str, Node] = dataclasses.field(default_factory=lambda: dict())

    def add_rule(self, before: str, after: str) -> Node:
        if before not in self._registry:
            self._registry[before] = Node(value=before)
        self._registry[before].after.add(after)
        return self._registry[before]

    def get_node(self, value) -> Node:
        return self._registry.get(value, Node(value))





if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        rows: list[list[str]] = []
        nodes_registry, completed_rules = NodesRegistry(), False
        for line in handle.read().splitlines():
            if completed_rules:
                rows.append(line.split(","))
            elif line == "":
                completed_rules = True
            else:
                before, after = line.split("|")
                nodes_registry.add_rule(before, after)

        rows_as_nodes: list[list[Node]] = [[nodes_registry.get_node(e) for e in r] for r in rows]
        good_mids, bad_mids = [], []
        for row in rows_as_nodes:
            sorted_row = sorted(row)
            mid_value = int(sorted_row[len(row) // 2].value)
            if row == sorted_row:
                good_mids.append(mid_value)
            else:
                bad_mids.append(mid_value)

        print(sum(good_mids), sum(bad_mids))

