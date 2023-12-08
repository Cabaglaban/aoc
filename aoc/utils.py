import os
import inspect

dirname = os.path.dirname(__file__)


def split_strip(x: str, d: str):
    return [i.strip() for i in x.split(d)]


def read_input(year: int | str, day: int | str, example: bool=False, sfx: str = ""):
    fname = ("example" if example else "input") + sfx
    if year is int:
        year = f"y{year}"
    if day is int:
        day = f"d{day:02d}"

    with open(os.path.join(dirname, year, day, fname)) as f:
        return [l.strip() for l in f.readlines()]


def read_day_input(example: bool = False, sfx: str = ""):
    fname = inspect.stack()[-1].filename
    if fname.endswith("solve.py"):
        d, y = fname.split("/")[::-1][1:3]
        return read_input(y, d, example, sfx)
    raise ValueError(f"failed to parse year/day from {fname}")
