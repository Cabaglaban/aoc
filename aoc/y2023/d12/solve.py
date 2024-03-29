from aoc.utils import *
from functools import partial, cache


def solve(rec: str, groups: list[int]):
    def handle_dot(idx: int, group: int, size: int):
        if size == 0:  # not in group, continue
            return _solve(idx + 1, group, size)
        elif group < len(groups) and groups[group] == size:  # end of group
            return _solve(idx + 1, group + 1, 0)
        return 0

    def handle_hash(idx: int, group: int, size: int):
        return _solve(idx + 1, group, size + 1)

    handlers = {"?": [handle_dot, handle_hash], ".": [handle_dot], "#": [handle_hash]}

    @cache
    def _solve(idx: int, group: int, size: int):
        if idx < len(rec):
            return sum(handler(idx, group, size) for handler in handlers[rec[idx]])
        # not ending in group || ending in group
        return (group == len(groups) and size == 0) or (group == len(groups) - 1 and groups[group] == size)

    return _solve(0, 0, 0)


def parse_line(line, fold_mul):
    rec, groups = split_strip(line, " ")
    return solve(
        "?".join([rec] * fold_mul),
        list(map(int, split_strip(groups, ","))) * fold_mul,
    )


for ex, fold_mul, p in generate_runs(args=[[(1, "P1"), (5, "P2")]]):
    print(
        f"[{p}][ex={int(ex)}] ",
        sum(read_day_input(ex, line_parser=partial(parse_line, fold_mul=fold_mul))),
    )
