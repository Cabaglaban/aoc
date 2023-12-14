from aoc.utils import *
from collections import Counter


def tilt_v(input: list, block_reset: int, block_add: int, rrange: range, round_cond: callable):
    for x in range(len(input[0])):
        block = block_reset
        for y in rrange:
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and round_cond(block, y):
                input[block + block_add][x] = "O"
                input[y][x] = "."
                block += block_add
                continue
            block = y

    return input


def tilt_n(input):
    return tilt_v(input, -1, 1, range(len(input)), lambda block, y: block < y - 1)


def tilt_s(input):
    rows = len(input)
    return tilt_v(input, rows, -1, range(rows - 1, -1, -1), lambda block, y: block > y + 1)


def tilt_h(input: list, block_reset: int, block_add: int, crange: range, round_cond: callable):
    for y in range(len(input)):
        block = block_reset
        for x in crange:
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and round_cond(block, x):
                input[y][block + block_add] = "O"
                input[y][x] = "."
                block += block_add
                continue
            block = x
    return input


def tilt_w(input):
    return tilt_h(input, -1, 1, range(len(input[0])), lambda block, x: block < x - 1)


def tilt_e(input):
    cols = len(input[0])
    return tilt_h(input, cols, -1, range(cols - 1, -1, -1), lambda block, x: block > x + 1)


def tilt_cycle(input):
    return tilt_e(tilt_s(tilt_w(tilt_n(input))))


def calc_n(input):
    return sum(Counter(l).get("O", 0) * (len(input) - i) for i, l in enumerate(input))


def solve1(input):
    input = [list(l) for l in input]
    return calc_n(tilt_n(input))


def solve2(input):
    input = [list(l) for l in input]
    seen, loop = [], []
    repeat = int(1e9)
    loop_sidx = -1

    for n in range(repeat):
        k = "\n".join("".join(l) for l in input)
        if k in seen:
            if loop_sidx < 0:  # loop start
                loop_sidx = n - 1

            if len(loop) and loop[0] == k:  # loop end
                break
            loop.append(k)

        seen.append(k)
        input = tilt_cycle(input)

    idx = (repeat - loop_sidx - 1) % len(loop)

    return calc_n([list(l) for l in loop[idx].split("\n")])


for ex, p, solver in generate_runs(example=[True, False], args=[[("P1", solve1), ("P2", solve2)]]):
    print(
        f"[{p}][ex={int(ex)}] ",
        solver(read_day_input(ex)),
    )
