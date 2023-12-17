from aoc.utils import *
from heapq import heappop as hpop,  heappush as hpush


def solve(grid: Grid, min_steps: int, max_steps: int):
    start, end = P((0, 0)), P((grid.w - 1, grid.h - 1))
    q = [(0, start, R), (0, start, D)]
    seen = set()

    while q:
        hl, p, d = hpop(q)
        if p == end:
            return hl
        if (p, d) in seen:
            continue

        seen.add((p, d))
        for nd in (x for x in [R, L, U, D] if x not in [d, -d]):
            nhl = hl

            for step in range(1, max_steps + 1):
                np = p + (nd * step)
                if not grid.in_bounds(np):
                    break
                nhl += int(grid.at(np))
                if step >= min_steps:
                    hpush(q, (nhl, np, nd))


for ex, p, args in generate_runs(args=[[("P1", (1, 3)), ("P2", (4, 10))]]):
    print(f"[{p}][ex={int(ex)}] ", solve(Grid.from_input(read_day_input(ex)), *args))
