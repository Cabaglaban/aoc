from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')

target = 'shiny gold'
demo_in = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip()

demo_in2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip()


def parse(idata):
    rows = idata.split('\n')
    bags = {}
    for r in rows:
        s = [i.strip() for i in r.split('bags', 1)]
        bag_name = s.pop(0)
        bags[bag_name] = {}

        s = (s.pop(0).replace('contain', '').replace('bags', '')
             .replace('bag', '').replace('.', '').strip())
        if s == 'no other':
            continue

        for cb in [i.strip() for i in s.split(', ')]:
            n, name = cb.split(' ', 1)
            bags[bag_name][name] = int(n)

    return bags


def find_a(idata):
    bags = parse(idata)
    candidates = {target}
    while True:
        new_candidates = set()
        for c in candidates:
            new_candidates.add(c)
            for bn, b in bags.items():
                if c in b:
                    new_candidates.add(bn)
                    # print('can be in', bn)

        if len(new_candidates) > len(candidates):
            candidates = {c for c in new_candidates}
        else:
            candidates = {c for c in new_candidates}
            break

    candidates.remove(target)
    return len(candidates)


def find_b(idata):
    allbags = parse(idata)

    def r(name, s=''):
        # print(f'{s}IN {name}')

        if not allbags[name]:
            # print(f'{s} empty')
            return 0

        result = 0
        for bn, n in allbags[name].items():
            rr = r(bn, s=s + ' ')
            # print(f'{s}{name} has: {n} * {bn} => {n} + {n} * {rr} = {n + n * rr}')
            result += (n * rr) + n

        return result

    # print(allbags)
    return r(target)


print('a', find_a(demo_in))
assert find_b(demo_in) == 32
assert find_b(demo_in2) == 126
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
