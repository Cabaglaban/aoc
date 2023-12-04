INPUT_FILE = "example"
INPUT_FILE = "input"


def split_strip(x: str, d: str):
    return [i.strip() for i in x.split(d)]


def parse_line(line: str):
    card_splitted = split_strip(line, ":")
    n_splitted = split_strip(card_splitted[1], "|")

    for i, n in enumerate(n_splitted):
        n_splitted[i] = set(map(int, [x for x in split_strip(n, " ") if x]))

    win = len(n_splitted[0] & n_splitted[1])
    return win


with open(INPUT_FILE) as f:
    input = [parse_line(l.strip()) for l in f.readlines()]

# part 1
print(sum(2 ** (win - 1) for win in input if win))

# part 2
copies = {i: 1 for i in range(1, len(input) + 1)}
for idx, win in enumerate(input, start=1):
    if not win:
        continue

    for cidx in range(idx + 1, idx + win + 1):
        copies[cidx] += copies[idx]

print(sum(copies.values()))
