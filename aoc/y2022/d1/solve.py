from aoc.utils import *
from collections import deque


def sum_groups(input):
    c = 0
    for line in input:
        if line:
            c += int(line)
        else:
            yield c
            c = 0
    yield c


def solve1(input):
    return max(deque(sum_groups(input)))


def solve2(input):
    return sum(sorted(deque(sum_groups(input)), reverse=True)[:3])


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex)))
