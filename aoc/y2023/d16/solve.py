from aoc.utils import *
import sys

sys.setrecursionlimit(4000)

U = (0, -1)
D = (0, 1)
R = (1, 0)
L = (-1, 0)


def print_grid(seen, w, h):
    grid = [["."] * w for _ in range(h)]
    for p, _ in seen:
        x, y = p
        grid[y][x] = "#"
    print("\n".join("".join(l) for l in grid), "\n")


def walk(grid, w, h, seen, pos, d):
    x, y = pos
    if x < 0 or x >= w or y < 0 or y >= h or (pos, d) in seen:
        return

    seen.add((pos, d))
    moves = []

    c = grid[y][x]
    if c == "." or (c == "|" and d[1]) or (c == "-" and d[0]):
        moves = [d]
    elif c == "|":
        moves = [U, D]
    elif c == "-":
        moves = [L, R]
    elif c == "/":
        moves = [{R: U, L: D, U: R, D: L}[d]]
    elif c == "\\":
        moves = [{R: D, L: U, U: L, D: R}[d]]

    for mx, my in moves:
        walk(grid, w, h, seen, (x + mx, y + my), (mx, my))


def solve(grid, w, h, start, d):
    seen = set()
    walk(grid, w, h, seen, start, d)
    return len({p for p, _ in seen})


def solve1(grid, w, h):
    return solve(grid, w, h, (0, 0), R)


def solve2(grid, w, h):
    res = 0
    for x in range(1, w - 1):
        res = max(res, solve(grid, w, h, (x, 0), D))
        res = max(res, solve(grid, w, h, (x, h - 1), U))

    for y in range(1, h - 1):
        res = max(res, solve(grid, w, h, (0, y), R))
        res = max(res, solve(grid, w, h, (w - 1, y), L))

    for s, dirs in [
        ((0, 0), [R, D]),
        ((w - 1, 0), [L, D]),
        ((0, h - 1), [R, U]),
        ((w - 1, h - 1), [L, U]),
    ]:
        for d in dirs:
            res = max(res, solve(grid, w, h, s, d))

    return res


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(*parse_grid(read_day_input(ex))))
