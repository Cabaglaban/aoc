import re
from aoc.utils import *
from itertools import combinations_with_replacement

RULE_RE = re.compile(r"(\w)([<>])(\d+):(\w+)")


def parse_input(input):
    w_raw, r_raw = split_strip(input, "\n\n")
    workflows = {}
    for w in split_strip(w_raw, "\n"):
        idx = w.index("{")
        name = w[:idx]
        rules = []
        for r in split_strip(w[idx + 1 : -1], ","):
            if ":" not in r:
                rules.append((None, r))
            else:
                s = list(RULE_RE.search(r).groups())
                s[1] = int.__lt__ if s[1] == "<" else int.__gt__
                s[2] = int(s[2])
                rules.append((s[:-1], s[-1]))
        workflows[name] = rules

    ratings = []
    for r in split_strip(r_raw, "\n"):
        ratings.append({x[0]: int(x[2:]) for x in r.strip("{}").split(",")})

    return workflows, ratings


def work_the_flow(workflow: list, rating: dict) -> str:
    for rule, ej in workflow[:-1]:
        v, op, n = rule
        if op(rating[v], n):
            return ej
    return workflow[-1][1]


def work_the_flows(workflows: dict, rating: dict):
    wname = "in"
    while wname in workflows:
        wname = work_the_flow(workflows[wname], rating)

    return wname


def solve1(input):
    workflows, ratings = parse_input(input)
    ret = dict(zip(list("xmas"), [0] * 4))
    for rat in ratings:
        if work_the_flows(workflows, rat) == "A":
            for v, n in rat.items():
                ret[v] += n
    return sum(ret.values())


def solve2(input):
    workflows, _ = parse_input(input)
    xmas = list("xmas")
    accepted = 0

    combos = combinations_with_replacement(range(4000), 4)

    for combo in combos:
        rat = dict(zip(xmas, combo))
        if work_the_flows(workflows, rat) == "A":
            accepted += 1
    return accepted


# for ex, p, solver in generate_runs(example=[True], args=[[("P1", solve1), ("P2", solve2)]]):
for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex, line_parser=False)))
