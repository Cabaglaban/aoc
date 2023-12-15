from aoc.utils import *

R = "A"
P = "B"
S = "C"

WIN_TABLE = {R: S, P: R, S: P}


def solve1(input):
    res = 0
    for g in input:
        [g := g.replace(*r) for r in [("X", R), ("Y", P), ("Z", S)]]
        a, b = split_strip(g, " ")
        if a == b:
            res += 3
        elif WIN_TABLE[b] == a:
            res += 6
        res += "ABC".index(b) + 1
    return res


def solve2(input):
    res = 0
    for a, b in (split_strip(g, " ") for g in input):
        match b:
            case "Y":
                res += 3
                b = a
            case "X":
                b = WIN_TABLE[a]
            case "Z":
                res += 6
                b = list(WIN_TABLE.keys())[list(WIN_TABLE.values()).index(a)]
        res += "ABC".index(b) + 1
    return res


for ex, p, solver in generate_runs(args=[[("P1", solve1), ("P2", solve2)]]):
    print(f"[{p}][ex={int(ex)}] ", solver(read_day_input(ex)))
