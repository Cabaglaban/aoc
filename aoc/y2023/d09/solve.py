from aoc.utils import *


def diff(line: list) -> tuple[list, bool]:
    d = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    return d, set(d) == {0}


def solve1(line: list):
    diffs, all_zero = diff(line)
    if all_zero:
        return line[-1]
    return line[-1] + solve1(diffs)


def solve2(line: list, start: bool = True):
    diffs, all_zero = diff(line)
    if all_zero:
        return 0
    r = diffs[0] - solve2(diffs, False)
    if not start:
        return r
    return line[0] - r


runs = [
    (True, solve1, "[part1] ex:"),
    (False, solve1, "[part1] input:"),
    (True, solve2, "[part2] ex:"),
    (False, solve2, "[part2] input:"),
]

for example, solver, run in runs:
    input = read_day_input(
        example,
        line_parser=lambda line: list(map(int, split_strip(line, " "))),
    )

    print(f"{run}\t", sum(solver(l) for l in input))
