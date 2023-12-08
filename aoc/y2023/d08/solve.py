import math
from itertools import repeat, chain
from aoc.utils import *


def solve(instr, network, pos, end_cond):
    for i, d in enumerate(chain.from_iterable(repeat(instr)), 1):
        pos = network[pos][d]
        if end_cond(pos):
            return i


def solve1(instr, network):
    return solve(instr, network, "AAA", lambda p: p == "ZZZ")


def solve2(instr, network):
    return math.lcm(*[solve(instr, network, sp, lambda p: p.endswith("Z")) for sp in network if sp.endswith("A")])


def parse_line(line: str):
    row = split_strip(line, "=")
    return row[0], split_strip(row[1].strip("()"), ",")


runs = [
    (True, "1", solve1, "[part1] ex:"),
    (False, "", solve1, "[part1] input:"),
    (True, "2", solve2, "[part2] ex:"),
    (False, "", solve2, "[part2] input:"),
]

for example, sfx, solver, run in runs:
    input = read_day_input(example, sfx)

    print(
        f"{run}\t",
        solver(
            list(input[0]),
            {k: {"L": v[0], "R": v[1]} for k, v in (parse_line(l) for l in input[2:])},
        ),
    )
