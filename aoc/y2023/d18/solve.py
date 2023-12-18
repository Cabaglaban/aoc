from aoc.utils import *
import math


def parse_line(line: str) -> tuple[P, int, str]:
    s = split_strip(line, " ")
    return (STR2DIR[s[0]], int(s[1]), s[2].strip("()"))


def solve(moves):
    pos = P((0, 0))
    edges = [(pos, 1)]
    edges += ((pos := pos + d * n, n) for d, n in moves)

    area = edges[-1][1]
    for i in range(1, len(edges)):
        e1, e2 = edges[i - 1], edges[i]
        p1, p2 = e1[0], e2[0]
        area += (p1.y + p2.y) * (p1.x - p2.x) + e1[1]

    return math.ceil(area / 2)


def solve1(moves):
    return solve((d, n) for d, n, _ in moves)


def solve2(moves):
    return solve(([R, D, L, U][int(c[-1])], int(c[1:-1], 16)) for *_, c in moves)


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex, line_parser=parse_line)))
