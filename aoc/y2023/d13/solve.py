from aoc.utils import *
from functools import partial


def is_mirrored(lst: list[int], idx: int, smudge_mode: bool):
    smudges = 0
    for i in range(idx + 1):
        try:
            if val := lst[idx - i] ^ lst[idx + i + 1]:
                smudges += 1 + (val & (val - 1))
                if smudges > 1:
                    return False
        except IndexError:
            break
    return smudges == 1 if smudge_mode else smudges == 0


def solve(group, mirror_fn=is_mirrored):
    rows = [0] * len(group)
    cols = [0] * len(group[0])

    for y, row in enumerate(group):
        for x, c in enumerate(row):
            v = int(c == ".")
            cols[x] <<= 1
            cols[x] |= v

            rows[y] <<= 1
            rows[y] |= v

    for lst, mul in [[cols, 1], [rows, 100]]:
        for i in range(0, len(lst) - 1):
            if mirror_fn(lst, i):
                return (i + 1) * mul


for ex, p, smudge in generate_runs(example=[True], args=[[("P1", False), ("P2", True)]]):
    groups = [g.split("\n") for g in "\n".join(read_day_input(ex)).split("\n\n")]
    print(
        f"[{p}][ex={int(ex)}] ",
        sum(solve(g, partial(is_mirrored, smudge_mode=smudge)) for g in groups),
    )
