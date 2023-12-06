from os import path as ospath
from multiprocessing import Pool

dirname = ospath.dirname(__file__)

INPUT_FILE = "example"
INPUT_FILE = "input"


def split_strip(x: str, d: str):
    return [i.strip() for i in x.split(d)]


def parse_line(line: str, part2: bool):
    nrow = split_strip(line, ":")[1]
    if not part2:
        return [int(x) for x in nrow.split()]
    return [int(nrow.replace(" ", ""))]


for part2 in [False, True]:
    with open(ospath.join(dirname, INPUT_FILE)) as f:
        input = list(zip(*[parse_line(l.strip(), part2) for l in f.readlines()]))

    solutions = 1
    for t, d in input:
        tt = []
        for r in [range(1, t), range(t, 0, -1)]:
            for s in r:
                n = s * (t - s)
                if n > d:
                    tt.append(s)
                    break
        print(t, d, tt)
        solutions *= tt[1] - tt[0] + 1
    print(solutions)
