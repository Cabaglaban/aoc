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

    def __getitem__(self, k):
        for ranges in self.ranges:
            dst, src, l = ranges
            if src <= k < src + l:
                return dst + k - src
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
    input, seed_range = args
    min_loc = math.inf
    for idx in tqdm.tqdm(seed_range):
        for loc in path:
            idx = input[loc][idx]
        min_loc = min(min_loc, idx)
    return min_loc

for job_size, part2 in [(1, False), (10**7, True)]:
    with open(ospath.join(dirname, INPUT_FILE)) as f:
        input = {}
        for group in f.read().strip().split("\n\n"):
            input.update(parse_group(group, part2))

    seed_ranges = []
    for seed_range in input["seeds"]:
        seed_ranges.extend(
          range(x, min(x+job_size, seed_range[-1] + 1)) for x in range(seed_range[0], seed_range[-1] + 1, job_size)
        )

    with Pool(10) as p:
        ret = p.map(solve, [
            (input, seed_range) for seed_range in input["seeds"]
        ])
    print(min(ret))
