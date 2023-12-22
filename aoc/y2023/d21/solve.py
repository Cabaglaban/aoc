from aoc.utils import *


def walk(grid: Grid, start: P, max_steps: int):
    q = [(start, 0)]
    end = set()
    seen = set()

    while q:
        p, steps = q.pop(0)
        if (p, steps) in seen:
            continue
        seen.add((p, steps))

        if steps == max_steps:
            end.add(p)
            continue

        for d in STR2DIR.values():
            pos = p + d
            if grid.at(pos) in "S.":
                q.append((pos, steps + 1))

    return len(end)


def solve1(grid: Grid, example: bool):
    start = [P((row.index("S"), y)) for y, row in enumerate(grid.grid) if "S" in row][0]
    return walk(grid, start, 6 if example else 64)


def solve2(grid: Grid, example: bool):
    pass


# for ex, p, solver in generate_runs(example=[True], args=[[("P1", solve1), ("P2", solve2)]]):
for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(Grid.from_input(read_day_input(ex)), ex))
