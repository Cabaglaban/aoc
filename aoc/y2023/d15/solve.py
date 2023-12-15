from aoc.utils import *
import re
from collections import defaultdict, deque

step_re = re.compile(r"(=|-)")


def hash_str(s: str):
    cur = 0
    for c in s:
        cur = ((cur + ord(c)) * 17) % 256
    return cur


def split_step(step: str) -> list[str, int, str, int | None]:
    splitted = step_re.split(step)
    if splitted[1] == "=":
        splitted[2] = int(splitted[2])
    splitted.insert(1, hash_str(splitted[0]))
    return splitted


def solve1(line: list[str]):
    yield from (hash_str(step) for step in line)


def solve2(line: list[str]):
    boxes = defaultdict(dict)
    for step in line:
        label, label_hash, sign, fl = split_step(step)
        if sign == "=":
            boxes[label_hash][label] = fl
        elif sign == "-" and label in boxes[label_hash]:
            del boxes[label_hash][label]

    for bi, box in boxes.items():
        for li, fl in enumerate(box.values(), 1):
            yield (bi + 1) * li * fl


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    line = read_day_input(ex, line_parser=lambda line: split_strip(line, ","))[0]
    print(f"[{p}][ex={int(ex)}] ", sum(deque(solver(line))))
