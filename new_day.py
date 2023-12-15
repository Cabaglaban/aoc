from argparse import ArgumentParser
from datetime import datetime
import requests
import os
import shutil

dirname = os.path.dirname(__file__)


if __name__ == "__main__":
    dt = datetime.now()

    parser = ArgumentParser()
    parser.add_argument("-y", "--year", default=dt.year)
    parser.add_argument("-d", "--day", default=dt.day)

    args = parser.parse_args()
    year = int(args.year)
    day = int(args.day)

    session = os.environ["AOC_SESSION"]

    res = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})
    res.raise_for_status()

    dst = os.path.join(dirname, "aoc", f"y{year}", f"d{day}")
    shutil.copytree(os.path.join(dirname, "aoc", "tmpl"), dst, dirs_exist_ok=True)

    with open(os.path.join(dst, "input"), "wb") as f:
        f.write(res.content)
