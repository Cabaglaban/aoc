from collections import Counter
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')

demo_in = """
16
10
15
5
1
11
7
19
6
12
4
""".strip()
demo_in2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()


def find_a(idata):
    adapters = sorted([int(i.strip()) for i in idata.split('\n')])
    c = Counter(b - a for a, b in zip([0, *adapters], adapters))
    # +1 for last connection
    return c[1] * (c[3] + 1)

def find_b(idata):
    adapters = sorted([int(i.strip()) for i in idata.split('\n')])

    c = Counter()
    c[0] = 1

    for a in adapters:
        # sum of prev connections
        c[a] += sum(c[i] for i in range(a - 3, a))
    return c[adapters[-1]]



print('a', find_a(demo_in))
print('b', find_b(demo_in))
print('b2', find_b(demo_in2))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
