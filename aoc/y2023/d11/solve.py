from aoc.utils import *
from itertools import combinations


def solve(input, n):
    cols = [x for x in range(len(input[0])) if all(row[x] == "." for row in input)]
    rows = [y for y, row in enumerate(input) if "#" not in row]
    galaxies = [(x, y) for y, row in enumerate(input) for x, c in enumerate(row) if c == "#"]

    def spaces(a, b):
        xmin, xmax = min(a[0], b[0]), max(a[0], b[0])
        ymin, ymax = min(a[1], b[1]), max(a[1], b[1])

        return sum(1 for c in cols if xmin < c < xmax) + sum(1 for r in rows if ymin < r < ymax)

    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) + n * spaces(a, b) for a, b in combinations(galaxies, 2))


runs = [
    (True, 1, "[part1] ex:"),
    (False, 1, "[part1] input:"),
    (True, 10 - 1, "[part2] ex:"),
    (True, 100 - 1, "[part2] ex:"),
    (False, 1_000_000 - 1, "[part2] input:"),
]

for example, spaces_mul, run in runs:
    print(f"{run}\t", solve(read_day_input(example), spaces_mul))
