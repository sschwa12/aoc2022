from typing import List, Tuple, NamedTuple

from utils import read_file

data = read_file('09')
parsed = []
for s in data:
    dir, moves = s.split()
    parsed.append((dir, int(moves)))


def _sign(v):
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    @property
    def signed(self):
        return Point(*map(_sign, self))


directions_map = {
    'R': Point(1, 0),
    'L': Point(-1, 0),
    'U': Point(0, 1),
    'D': Point(0, -1)
}


def move_tail(head, tail):
    if max(map(abs, head - tail)) == 1:
        return tail
    return tail + (head - tail).signed


def num_positions_visited(directions: List[Tuple[str, int]]) -> int:
    visited = set()
    head = tail = Point(0, 0)
    for direction, moves in directions:
        p = directions_map[direction]
        for _ in range(moves):
            head += p
            tail = move_tail(head, tail)
            visited.add(tail)
    return len(visited)


p1 = num_positions_visited(parsed)
print(p1)
