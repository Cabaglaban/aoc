import re
from aoc.utils import *
from math import prod

RULE_RE = re.compile(r"(\w)([<>])(\d+):(\w+)")

create_rating = lambda val: {i: val for i in "xmas"}


def lt(a: int | range, b: int) -> bool | tuple[range, range]:
    return a < b if isinstance(a, int) else (range(a[0], min(a[-1], b)), range(max(a[0], b), a[-1] + 1))


def gt(a: int | range, b: int) -> bool | tuple[range, range]:
    return a > b if isinstance(a, int) else (range(max(a[0], b + 1), a[-1] + 1), range(a[0], min(a[-1], b) + 1))


def parse_rules(s):
    for r in split_strip(s, ","):  # s>2770:qs,m<1801:hdj,R
        if ":" not in r:
            yield (None, r)
        else:
            v, op, n, ej = list(RULE_RE.search(r).groups())
            yield ((v, {"<": lt, ">": gt}[op], int(n)), ej)


def parse_input(input):
    w_raw, r_raw = split_strip(input, "\n\n")
    workflows = {}
    for w in split_strip(w_raw, "\n"):  # qqz{s>2770:qs,m<1801:hdj,R}
        idx = w.index("{")
        workflows[w[:idx]] = list(parse_rules(w[idx + 1 : -1]))

    return (
        workflows,
        [  # {x=787,m=2655,a=1222,s=2876}
            {x[0]: int(x[2:]) for x in r.strip("{}").split(",")} for r in split_strip(r_raw, "\n")
        ],
    )


def work_the_flows(workflows: dict, wname: str, rating: dict):
    def flow(workflow: list, rating: dict) -> str:
        for (v, op, n), ej in workflow[:-1]:
            if op(rating[v], n):
                return ej
        return workflow[-1][1]

    while wname in workflows:
        wname = flow(workflows[wname], rating)
    return wname


def solve1(workflows, ratings):
    return sum(sum(rat.values()) for rat in ratings if work_the_flows(workflows, "in", rat) == "A")


def work_the_bounds(workflows, name, xmas):
    if name == "R":
        yield 0
    elif name == "A":
        yield prod(len(i) for i in xmas.values())
    else:
        for (v, op, n), ej in workflows[name][:-1]:
            as_true = xmas.copy()
            as_true[v], xmas[v] = op(xmas[v], n)

            yield from work_the_bounds(workflows, ej, as_true)
        yield from work_the_bounds(workflows, workflows[name][-1][1], xmas)


def solve2(workflows, _):
    return sum(work_the_bounds(workflows, "in", create_rating(range(1, 4001))))


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(*parse_input(read_day_input(ex, line_parser=False))))
