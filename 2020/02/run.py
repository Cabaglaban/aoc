demo_in = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".strip().split('\n')


def is_valid(pswd: str):
    r, ch, s = pswd.replace(':', '').split(' ')
    mi, ma = list(map(int, r.split('-')))

    return mi <= s.count(ch) <= ma


def is_valid_b(pswd: str):
    p, ch, s = pswd.replace(':', '').split(' ')
    p1, p2 = list(map(int, p.split('-')))

    # if len(s) < p2:
    #     return False

    print(s, s[p1 - 1] == ch, s[p2 - 1] == ch)

    return (s[p1 - 1] == ch) ^ (s[p2 - 1] == ch)


def count(idata):
    return sum([is_valid(r) for r in idata])


def count_b(idata):
    return sum([is_valid_b(r) for r in idata])


print(count(demo_in))
print(count_b(demo_in))
with open('in', 'r') as f:
    r = f.readlines()
    print(count(r))
    print(count_b(r))
