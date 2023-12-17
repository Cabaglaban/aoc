import os
import re
import inspect
from itertools import product
from collections.abc import Iterable, Callable

dirname = os.path.dirname(__file__)
RE_SPACE = re.compile(r"\s+")


def split_strip(x: str, d: str | re.Pattern, cast=str):
    return [cast(i.strip()) for i in (d.split(x) if isinstance(d, re.Pattern) else x.split(d))]


def parse_grid(lines: list[str]) -> tuple[list[str], int, int]:
    return lines, len(lines[0]), len(lines)


def read_input(
    year: int | str, day: int | str, example: bool = False, sfx: str = "", line_parser: bool | Callable | None = None
):
    fname = ("example" if example else "input") + sfx
    if year is int:
        year = f"y{year}"
    if day is int:
        day = f"d{day:02d}"

    with open(os.path.join(dirname, year, day, fname)) as f:
        if line_parser is None:
            lines = [l.strip() for l in f.readlines()]
            if callable(line_parser):
                lines = [line_parser(l) for l in lines]
            return lines
        return f.read()


def read_day_input(example: bool = False, sfx: str = "", line_parser: bool | Callable | None = None):
    fname = inspect.stack()[-1].filename
    if fname.endswith("solve.py"):
        d, y = fname.split("/")[::-1][1:3]
        return read_input(y, d, example, sfx, line_parser)
    raise ValueError(f"failed to parse year/day from {fname}")


def generate_runs(args, example=[True, False]):
    for p in product(example, *args):
        r = []
        for i in p:
            if not isinstance(i, Iterable):
                i = [i]
            r.extend(i)
        yield r


class P(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def p(self):
        return (self.x, self.y)

    def __add__(self, v):
        if isinstance(v, tuple):
            v = P(v)

        return P((self.x + v.x, self.y + v.y))

    def __mul__(self, v):
        assert isinstance(v, int)
        return P((self.x * v, self.y * v))

    def __neg__(self):
        return P((-self.x, -self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


U = P((0, -1))
R = P((1, 0))
D = P((0, 1))
L = P((-1, 0))


class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.w = len(grid[0])
        self.h = len(grid)

    @staticmethod
    def from_input(input):
        return Grid(input)

    def in_bounds(self, p):
        return self._in_bounds(*(p.p if isinstance(p, P) else p))

    def _in_bounds(self, x, y):
        return (0 <= x <= self.w - 1) and (0 <= y <= self.h - 1)

    def at(self, p, oob="out-of-bounds"):
        x, y = p.p if isinstance(p, P) else p
        if not self._in_bounds(x, y):
            return oob
        return self.grid[y][x]
