from aoc.utils import *
import re

move_re = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse(input):
    stack, steps = input.split("\n\n")
    steps = [list(map(int, move_re.findall(s)[0])) for s in split_strip(steps.strip(), "\n")]
    stack = stack.split("\n")
    stack_n = split_strip(stack[-1].strip(" "), RE_SPACE, int)[-1]
    boxes = [[] for _ in range(stack_n)]
    for s in stack[:-1]:
        for i in range(0, stack_n + 2 // 4):
            box = s[4 * i + 1 : 4 * i + 2]
            if box != " ":
                boxes[i].append(box)
    return steps, [None] + boxes


def solve1(input):
    steps, boxes = parse(input)
    for cnt, f, t in steps:
        for _ in range(cnt):
            boxes[t].insert(0, boxes[f].pop(0))
    return "".join(b[0] for b in boxes[1:] if len(b))


def solve2(input):
    steps, boxes = parse(input)
    for cnt, f, t in steps:
        boxes[t] = boxes[f][0:cnt] + boxes[t]
        boxes[f] = boxes[f][cnt:]
    return "".join(b[0] for b in boxes[1:] if len(b))


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex, line_parser=False)))
