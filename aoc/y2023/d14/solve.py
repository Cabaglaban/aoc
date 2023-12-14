from aoc.utils import *
from collections import Counter


def tilt_n(input):
    for x in range(len(input[0])):
        block = -1
        for y in range(len(input)):
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and block < y - 1:
                input[block + 1][x] = "O"
                input[y][x] = "."
                block += 1
                continue
            block = y

    return input


def tilt_s(input):
    rows = len(input)
    for x in range(len(input[0])):
        block = rows
        for y in range(rows - 1, -1, -1):
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and block > y + 1:
                input[block - 1][x] = "O"
                input[y][x] = "."
                block -= 1
                continue
            block = y
    return input


def tilt_w(input):
    for y in range(len(input)):
        block = -1
        for x in range(len(input[0])):
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and block < x - 1:
                input[y][block + 1] = "O"
                input[y][x] = "."
                block += 1
                continue
            block = x

    return input


def tilt_e(input):
    cols = len(input[0])
    for y in range(len(input)):
        block = cols
        for x in range(cols - 1, -1, -1):
            if input[y][x] == ".":
                continue
            if input[y][x] == "O" and block > x + 1:
                input[y][block - 1] = "O"
                input[y][x] = "."
                block -= 1
                continue
            block = x
    return input


def tilt_cycle(input):
    return tilt_e(tilt_s(tilt_w(tilt_n(input))))


def calc_n(input):
    return sum(Counter(l).get("O", 0) * (len(input) - i) for i, l in enumerate(input))


def solve1(input):
    input = [list(l) for l in input]
    return calc_n(tilt_n(input))


def solve2(input):
    input = [list(l) for l in input]
    seen = []
    repeat = int(1e9)
    loop_sidx = -1
    loop = []

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
