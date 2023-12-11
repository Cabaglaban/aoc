from aoc.utils import *

W = (-1, 0)
N = (0, -1)
E = (1, 0)
S = (0, 1)

SPACE = "."

ALLOWED = {
    N: "|7FS",
    S: "|LJS",
    E: "-J7S",
    W: "-FLS",
}

PIPES = {
    "|": (N, S),
    "-": (W, E),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    "S": (W, N, E, S),
}

EDGES = {"F": "J", "L": "7"}
CONNECTIONS = {
    (N, S): "|",
    (W, E): "-",
    (N, E): "L",
    (N, W): "J",
    (S, E): "F",
    (S, W): "7",
}


def find_start(input):
    for y, row in enumerate(input):
        if "S" in row:
            return (row.index("S"), y)
    raise ValueError("start not found!")


def get_neighbors(input, coords):
    x, y = coords
    neighbors = dict(zip([N, W, S, E], [""] * 4))
    if x - 1 >= 0:
        neighbors[W] = input[y][x - 1]
    if x + 1 <= len(input[y]) - 1:
        neighbors[E] = input[y][x + 1]
    if y - 1 >= 0:
        neighbors[N] = input[y - 1][x]
    if y + 1 <= len(input) - 1:
        neighbors[S] = input[y + 1][x]
    return neighbors


def get_valid_moves(input, coords):
    x, y = coords
    pipe = input[y][x]

    neighbors = get_neighbors(input, coords)
    return [(d[0] + x, d[1] + y) for d in PIPES[pipe] if neighbors[d] and neighbors[d] in ALLOWED[d]]


def get_free_moves(input, coords):
    x, y = coords
    neighbors = get_neighbors(input, coords)
    return [(d[0] + x, d[1] + y) for d in neighbors if neighbors[d] == SPACE]


def is_valid_pipe(input, coords):
    x, y = coords
    pipe = input[y][x]

    if pipe in ["S", SPACE]:
        return True
    elif pipe in PIPES:
        neighbors = get_neighbors(input, coords)
        return all(neighbors[d] in ALLOWED[d] for d in PIPES[pipe])


def clear_maze(input):
    cleared = []

    for y in range(len(input)):
        cleared.append("")
        for x in range(len(input[0])):
            p = SPACE
            if is_valid_pipe(input, (x, y)):
                p = input[y][x]
            cleared[y] += p
    return cleared


def solve1(input):
    start = find_start(input)
    moves = get_valid_moves(input, start)
    seen = {start}
    n = 1

    while True:
        next_moves = []
        for d in (m for m in moves if m not in seen):
            seen.add(d)
            next_moves.extend(get_valid_moves(input, d))

        moves = next_moves
        if not moves:
            return n - 1, seen

        n += 1


def solve2(input):
    maze = [["."] * len(input[0]) for _ in input]
    _, loop = solve1(input)

    # keep just winning loop in maze
    for x, y in loop:
        maze[y][x] = input[y][x]

    # replace start
    start = find_start(input)
    neighbors = {(m[0] - start[0], m[1] - start[1]) for m in get_valid_moves(input, start)}
    connections = [pipe for c, pipe in CONNECTIONS.items() if neighbors == set(c)]
    assert len(connections) == 1, f"could not determine start pipe from start neighbors {neighbors}"
    maze[start[1]][start[0]] = connections[0]

    enclosed = 0
    for y, row in enumerate(maze):
        in_loop = False
        edge = None

        for x, c in enumerate(row):
            if c == "." and in_loop:
                enclosed += 1
            elif c == "|":
                in_loop = not in_loop
            elif c in EDGES:
                edge = c
            elif c in EDGES.values():
                edge = None
                if edge and EDGES[edge] == c:
                    in_loop = not in_loop

    return enclosed, None


runs = [
    (True, solve1, "1", "[part1] ex:"),
    (False, solve1, "", "[part1] input:"),
    (True, solve2, "2", "[part2] ex:"),
    (False, solve2, "", "[part2] input:"),
]

for example, solver, sfx, run in runs:
    input = read_day_input(example, sfx=sfx)
    cleared = clear_maze(input)

    res, _ = solver(cleared)

    print(f"{run}\t", res)
