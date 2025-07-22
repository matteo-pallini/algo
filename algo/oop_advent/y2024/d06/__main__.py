import dataclasses
from collections import defaultdict
from itertools import chain
from typing import DefaultDict


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(x=self.x+other.x, y=self.y+other.y)

    def __hash__(self) -> int:
        return hash(f"{self.x}_{self.y}")


class Map:
    def __init__(self, map: list[list[str]]):
        self._map = map
        self.vertical_edge = len(self._map)
        self.horizontal_edge = len(self._map[0])
        self.potential_obstacles: set = set()

    def step_hits_boundary(self, point: Point) -> bool:
        return self.horizontal_edge <= point.x or point.x < 0 or self.vertical_edge <= point.y or point.y < 0

    def step_hits_obstacle(self, point: Point) -> bool:
        if self.step_hits_boundary(point):
           raise ValueError(f"Step {point} goes outside of map")
        return self._map[point.y][point.x] == "#"


@dataclasses.dataclass
class Guard:
    position: Point
    step_direction: Point = dataclasses.field(default_factory=lambda: Point(0, -1))
    visited: DefaultDict[Point, set[Point]] = dataclasses.field(default_factory=lambda: defaultdict(set))
    counter: int = 0

    def take_next_step(self) -> Point:
        return self.position + self.step_direction

    def move_to_position(self, point: Point):
        self.position = point
        self.visited[self.step_direction].add(point)

    def turn(self):
        self.step_direction = self._future_turn()
        self.visited[self.step_direction].add(self.position)

    def _future_turn(self):
        match self.step_direction:
            case Point(0, -1):
                return Point(1, 0)
            case Point(1, 0):
                return Point(0, 1)
            case Point(0, 1):
                return Point(-1, 0)
            case Point(-1, 0):
                return Point(0, -1)
            case _:
                raise ValueError(f"{self.step_direction} is not a supported direction")

    def check_for_potential_obstacle(self, next_position: Point, map: Map) -> Point | None:
        # print(self.position, self.position + self._future_turn(), self._future_turn(), self.visited[self._future_turn()])
        if (self.position + self._future_turn()) in self.visited[self._future_turn()]:
            return next_position
        # print(next_position, self.visited[self.step_direction])
        # print("\n")
        if next_position in self.visited[self.step_direction]:
            return next_position
        if self._will_hit_previous_route(self.position + self._future_turn(), step_direction=self._future_turn(), map=map):
            return next_position

    def _will_hit_previous_route(self, position: Point, step_direction: Point, map: Map):
        next_step = position + step_direction
        while not map.step_hits_boundary(next_step) and not map.step_hits_obstacle(next_step):
            if next_step in self.visited[step_direction]:
                return True
            next_step += step_direction


if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        rows = [[e for e in line] for line in handle.read().splitlines()]
        for idx_row, row in enumerate(rows):
            for idx, p in enumerate(row):
                if p == "^":
                    starting_point = Point(x=idx, y=idx_row)
        guard = Guard(position=starting_point)
        guard.visited[guard.step_direction].add(starting_point)
        map = Map(rows)
        while not map.step_hits_boundary(guard.take_next_step()):
            step = guard.take_next_step()
            if not map.step_hits_boundary(step):
                if map.step_hits_obstacle(step):
                    guard.turn()
                else:
                    if potential_obstacle := guard.check_for_potential_obstacle(step, map=map):
                        map.potential_obstacles.add(potential_obstacle)
                    guard.move_to_position(step)
        print(len(set(chain.from_iterable([e for e in guard.visited.values()]))))
        print(len(map.potential_obstacles))







