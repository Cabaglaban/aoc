from aoc.utils import *


def score(x: str):
    if x.lower() == x:
        return ord(x) - 96
    return ord(x) - 38


def solve1(input):
    n = 0
    for r in input:
        l = len(r) // 2
        n += score((set(r[:l]) & set(r[l:])).pop())
    return n


def solve2(input):
    n = 0
    for i in range(0, len(input), 3):
        a, b, c = tuple(map(set, input[i : i + 3]))
        n += score((a & b & c).pop())
    return n


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex)))
