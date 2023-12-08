from functools import reduce
import os
import re

in_file = os.path.join(os.path.dirname(__file__), 'in')

expected_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",  # optional
}

demo_in = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip()


def find_a(idata):
    idata = (" ".join(idata.split("\n"))).split("  ")
    good = 0
    for record in idata:
        keys = {item.split(':')[0] for item in record.split(' ')}
        missing = expected_fields - keys

        # still good
        if missing == {'cid'} or not missing:
            good += 1

    return good


def find_b(idata):
    idata = (" ".join(idata.split("\n"))).split("  ")
    good = 0
    for record in idata:
        keys = {item.split(':')[0] for item in record.split(' ')}
        missing = expected_fields - keys

        if missing == {'cid'} or not missing:
            valid = True
            try:
                for k, v in (i.split(':') for i in record.split(' ')):
                    ov = v
                    if k == 'byr':
                        v = int(v)
                        if v < 1920 or v > 2002:
                            raise Exception(f"{k} - {ov}")
                    if k == 'iyr':
                        v = int(v)
                        if v < 2010 or v > 2020:
                            raise Exception(f"{k} - {ov}")
                    if k == 'eyr':
                        v = int(v)
                        if v < 2020 or v > 2030:
                            raise Exception(f"{k} - {ov}")
                    if k == 'hgt':
                        if v.endswith('cm'):
                            v = int(v[0:-2])
                            if v < 150 or v > 193:
                                raise Exception(f"{k} - {ov}")
                        elif v.endswith('in'):
                            v = int(v[0:-2])
                            if v < 59 or v > 76:
                                raise Exception(f"{k} - {ov}")
                        else:
                            raise Exception(f"{k} - {ov}")
                    if k == 'hcl' and not re.match('#[0-9a-f]{6}', v):
                        raise Exception(f"{k} - {ov}")
                    if k == 'ecl' and v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        raise Exception(f"{k} - {ov}")
                    if k == 'pid' and not re.match('^[0-9]{9}$', v):
                        raise Exception(f"{k} - {ov}")
            except Exception as e:
                valid = False

            good += 1 if valid else 0
    return good

print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
