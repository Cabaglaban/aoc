from collections import Counter
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')


demo_in = """
abc

a
b
c

ab
ac

a
a
a
a

b
""".strip()


def find_a(idata):
    return sum(
        [
            len(Counter(g.replace('\n', ''))) for g in idata.split('\n\n')
        ]
    )


def find_b(idata):
    groups = [g.split('\n') for g in idata.split('\n\n')]
    answers = 0
        
    for g in groups:
        answers += len(set.intersection(*[set(i) for i in g]))
    return answers
    


print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
