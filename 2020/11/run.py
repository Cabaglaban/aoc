from collections import Counter
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')
DEBUG = False
demo_in = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]


def count_occupied_adj(rows, x, y):
    occ = 0
    for i, j in DIRS:
        if y + j < 0 or x + i < 0:
            continue
        # print(f'\t {x+i}.{y+j} == {rows[y + j][x + i]}')
        try:
            occ += 1 if rows[y + j][x + i] == '#' else 0
        except IndexError:
            pass

    return occ

if DEBUG:
	assert count_occupied_range("""
	.......#.
	...#.....
	.#.......
	.........
	..#L....#
	....#....
	.........
	#........
	...#.....
	    """.strip().split('\n'), 3, 4
	                            ) == 8
	assert count_occupied_range("""
	.............
	.L.L.#.#.#.#.
	.............
	""".strip().split('\n'), 1, 1
	                            ) == 0
	assert count_occupied_range("""
	.##.##.
	#.#.#.#
	##...##
	...L...
	##...##
	#.#.#.#
	.##.##.
	""".strip().split('\n'), 3, 3
                            ) == 0


def count_occupied_range(rows, x, y):
    occ = 0
    for i, j in DIRS:
        nx, ny = x, y
        while True:
            if ny + j < 0 or nx + i < 0:
                break
            try:
                s = rows[ny + j][nx + i]
                if s == 'L':
                    break
                elif s == '#':
                    occ += 1
                    break
                nx += i
                ny += j
            except IndexError:
                break

    return occ


def find_a(idata, count_f=count_occupied_adj, limit=4):
    rows = [r.strip() for r in idata.split('\n')]

    while True:
        new_rows = rows[:]

        for y, r in enumerate(new_rows):
            new_row = ''
            for x, s in enumerate(r):
                if s == '.':
                    new_row += s
                    continue
                occ = count_f(rows, x, y)
                DEBUG and print(f'{s} at {x}.{y} has {occ}')

                if s == 'L' and occ == 0:
                    new_row += '#'
                elif s == '#' and occ >= limit:
                    new_row += 'L'
                else:
                    new_row += s
            new_rows[y] = new_row

        DEBUG and print('\n'.join(new_rows), '\n')
        if new_rows == rows:
            return Counter(''.join(new_rows))['#']

        rows = new_rows


def find_b(idata):
    return find_a(idata, count_occupied_range, limit=5)

print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
