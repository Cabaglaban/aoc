from os import path as ospath
import sys
from collections import Counter
from functools import cmp_to_key

dirname = ospath.dirname(__file__)

INPUT_FILE = "example"
INPUT_FILE = "input"

FACE_TO_NUM = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    **{str(i): i for i in range(10)}
}

def score(item):
    c = Counter(item).values()

    if 5 in c:
        return 7
    elif 4 in c:
        return 6
    elif 3 in c and 2 in c:
        return 5
    elif 3 in c:
        return 4
    elif Counter(c).get(2) == 2:
        return 3
    elif 2 in c:
        return 2
    return 1

def find_highest_joker_score(card):
    s = [score(card)]
    s.extend(score(card.replace("J", c)) for c in {c for c in card.replace("J", "")})
    return max(s)

score_func = score
if len(sys.argv) == 2:
    score_func = find_highest_joker_score
    FACE_TO_NUM["J"] = 0

def score_cmp(item1, item2):
    a, b = item1[0], item2[0]
    sa, sb = score_func(a), score_func(b)
 
    if sa == sb:
        for aa, bb in zip(a, b):
            if aa == bb:
                continue
            return 1 if FACE_TO_NUM[aa] > FACE_TO_NUM[bb] else -1

    return 1 if sa > sb else -1

def split_strip(x: str, d: str):
    return [i.strip() for i in x.split(d)]


def parse_line(line: str):
    row = split_strip(line, " ")
    return (row[0], int(row[1]))


with open(ospath.join(dirname, INPUT_FILE)) as f:
    input = [parse_line(l.strip()) for l in f.readlines()]

input.sort(key=cmp_to_key(score_cmp))
win = (idx * hand[1] for idx, hand in enumerate(input, start=1))
print(sum(win))
