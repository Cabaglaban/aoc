from os import path as ospath
import math
import tqdm
from multiprocessing import Pool

dirname = ospath.dirname(__file__)

INPUT_FILE = "example"
INPUT_FILE = "input"

class MDict:
    def __init__(self, ranges) -> None:
        self.ranges = sorted(ranges, key=lambda item: item[0])

    def next(self, k):
        for dst, src, l in self.ranges:
            if src <= k < src + l:
                return dst + k - src
        return k

    def prev(self, k):
        for dst, src, l in self.ranges:
            if dst <= k < dst + l:
                return src + k - dst
        return k


def split_strip(x: str, d: str):
    return [i.strip() for i in x.split(d)]


def parse_group(group: str, part2: bool):
    lines = group.split("\n")
    if lines[0].startswith("seeds:"):
        seeds = list(map(int, split_strip(lines[0].replace("seeds: ", ""), " ")))
        if not part2:
            return {"seeds": [range(seed, seed + 1) for seed in seeds]}
        else:
            return {"seeds": [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]}
    elif lines[0].endswith("map:"):
        return {
            lines[0].replace(" map:", ""): MDict(
                [tuple(map(int, split_strip(line, " "))) for line in lines[1:]],
            )
        }

    return {}


path = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]

def solve(args):
    input, range_to_solve = args
    for s_idx in range_to_solve:
        idx = s_idx
        for loc in reversed(path):
            idx = input[loc].prev(idx)

        if any(idx in seeds for seeds in input["seeds"]):
            print(f"found {s_idx}")
            return s_idx

    return math.inf

for part2 in [False, True]:
    with open(ospath.join(dirname, INPUT_FILE)) as f:
        input = {}
        for group in f.read().strip().split("\n\n"):
            input.update(parse_group(group, part2))

    step = 10**7
    with Pool() as p:
        ret = p.map(solve, [
            (input, r) for r in (range(x, x+step) for x in range(0, 10**9, step))
        ])
    print(min(ret))
