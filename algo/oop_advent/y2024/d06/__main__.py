import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(x=self.x+other.x, y=self.y+other.y)

    def __hash__(self) -> int:
        return hash(f"{self.x}_{self.y}")


@dataclasses.dataclass
class Guard:
    position: Point
    step_direction: Point = dataclasses.field(default_factory=lambda: Point(0, -1))
    visited: set[Point] = dataclasses.field(default_factory=lambda: set())

    def take_next_step(self) -> Point:
        return self.position + self.step_direction

    def move_to_position(self, point: Point):
        self.position = point
        self.visited.add(point)

    def turn(self):
        match self.step_direction:
            case Point(0, -1):
                self.step_direction = Point(1, 0)
            case Point(1, 0):
                self.step_direction = Point(0, 1)
            case Point(0, 1):
                self.step_direction = Point(-1, 0)
            case Point(-1, 0):
                self.step_direction = Point(0, -1)
            case _:
                raise ValueError(f"{self.step_direction} is not a supported direction")


class Map:

    def __init__(self, map: list[list[str]]):
        self._map = map
        self.vertical_edge = len(self._map)
        self.horizontal_edge = len(self._map[0])

    def step_hits_boundary(self, point: Point) -> bool:
        return self.horizontal_edge <= point.x or point.x < 0 or self.vertical_edge <= point.y or point.y < 0

    def step_hits_obstacle(self, point: Point) -> bool:
        if self.step_hits_boundary(point):
           raise ValueError(f"Step {point} goes outside of map")
        return self._map[point.y][point.x] == "#"


if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        rows = [[e for e in line] for line in handle.read().splitlines()]
        for idx_row, row in enumerate(rows):
            for idx, p in enumerate(row):
                if p == "^":
                    starting_point = Point(x=idx, y=idx_row)
        guard = Guard(position=starting_point, visited={starting_point})
        map = Map(rows)
        while not map.step_hits_boundary(guard.take_next_step()):
            step = guard.take_next_step()
            if not map.step_hits_boundary(step):
                if map.step_hits_obstacle(step):
                    guard.turn()
                else:
                    guard.move_to_position(step)
        print(len(guard.visited))







