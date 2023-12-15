from aoc.utils import *


def solve1(input):
    pass


def solve2(input):
    pass


for ex, p, solver in generate_runs(example=[True], args=[[("P1", solve1), ("P2", solve2)]]):
# for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex)))
