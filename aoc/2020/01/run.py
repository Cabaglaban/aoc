demo_in = """
1721
979
366
299
675
1456
""".strip().split('\n')


def find_a(idata):
    for a in idata:
        for b in idata:
            if a + b == 2020:
                print(f'{a} * {b} == {a * b}')
                return

def find_b(idata):
    for a in idata:
        for b in idata:
            for c in idata:
                if a + b + c == 2020:
                    print(f'{a} * {b} * {c} == {a * b * c}')
                    return


# idata = map(int, demo_in)
with open('in_1', 'r') as f:
    x = list(map(int, f.readlines()))
    find_a(x)
    find_b(x)

