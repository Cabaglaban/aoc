from aoc.utils import *
from itertools import combinations
from itertools import chain


def solve(input, n):
    n = n - 1 if n > 1 else n
    cols = [int(all(row[x] == "." for row in input)) for x in range(len(input[0]))]
    rows = [int("#" not in row) for row in input]
    galaxies = [(x, y) for y, row in enumerate(input) for x, c in enumerate(row) if c == "#"]

    def calc(a, b):
        xmin, xmax, ymin, ymax = chain.from_iterable(sorted(i) for i in zip(a, b))
        return (xmax - xmin) + (ymax - ymin) + n * (sum(cols[xmin:xmax]) + sum(rows[ymin:ymax]))

    return sum(calc(a, b) for a, b in combinations(galaxies, 2))


runs = [
    (True, 1, "[part1] ex:"),
    (False, 1, "[part1] input:"),
    (True, 10, "[part2] ex:"),
    (True, 100, "[part2] ex:"),
    (False, 1_000_000, "[part2] input:"),
]

for example, spaces_mul, run in runs:
    print(f"{run}\t", solve(read_day_input(example), spaces_mul))
