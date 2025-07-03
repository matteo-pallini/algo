import math
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        self.memo = {}

        def _move_forward(color, idx):
            next_color = "red" if color == "blue" else "blue"
            if idx <= 0:
                return 0
            if (color, idx) in self.memo:
                return self.memo[(color, idx)]
            options = mapper[color].get(idx, set())
            value = math.inf
            for opt in options:
                if opt == idx:
                    self.memo[(color, idx)] = math.inf
                    continue
                val = _move_forward(next_color, opt)
                self.memo[(color, idx)] = val+1
                value = min(value, self.memo[(color, idx)])
                print(opt, idx, self.memo, value)
            return value

        mapper = {
            "blue": self._build_mapping(blue_edges),
            "red": self._build_mapping(red_edges)
        }
        final_vals = []
        for idx in range(n):
            final_vals.append(
                min(_move_forward("blue", idx), _move_forward("red", idx))
            )
        return [e if e != math.inf else -1 for e in final_vals]

    def _build_mapping(self, edges):
        mapping = {}
        for (start, end) in edges:
            if end not in mapping:
                mapping[end] = set([start])
            else:
                mapping[end].add(start)
        print(mapping)
        return mapping
