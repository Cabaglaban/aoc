from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')

expected_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid", optional
]

demo_in = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()


def find_a(idata):
    print(idata.split("\n"))


def find_b(idata):
    pass


print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = [r.strip() for r in f.readlines()]
    # print('a', find_a(x))
    # print('b', find_b(x))
