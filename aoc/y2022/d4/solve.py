from aoc.utils import *


def inr(x, r):
    return r[0] <= x <= r[1]


def solve(input: list, cmp: callable):
    return sum(
        cmp(
            *[split_strip(x, "-", cast=int) for x in split_strip(l, ",")],
        )
        for l in input
    )


def solve1(input):
    return solve(input, lambda a, b: (inr(a[0], b) and inr(a[1], b)) or (inr(b[0], a) and inr(b[1], a)))


def solve2(input):
    return solve(input, lambda a, b: inr(a[0], b) or inr(a[1], b) or inr(b[0], a) or inr(b[1], a))


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex)))
