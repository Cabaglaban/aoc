from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')


demo_in = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()

def find_sum(x, n):
    for a in n:
        for b in n:
            if a + b == x:
                return True
    return False

def find_a(idata, preamble):
    numbers = [int(n.strip()) for n in idata.split("\n")]
    idx = preamble
    
    while idx < len(numbers):
        correct = find_sum(numbers[idx], numbers[idx-preamble:idx])
        if not correct:
            # print(f'found error at {idx} => {numbers[idx]}')
            return idx, numbers[idx]
        idx += 1
        

def find_b(idata, preamble):
    numbers = [int(n.strip()) for n in idata.split("\n")]
    _, invalid = find_a(idata, preamble)
    
    for ai, a in enumerate(numbers):
        p = [a]
        for b in numbers[ai + 1:]:
            p.append(b)
            s = sum(p)
            
            if s == invalid:
                return min(p) + max(p)
            elif s > invalid:
                break


print('a', find_a(demo_in, 5))
print('b', find_b(demo_in, 5))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x, 25))
    print('b', find_b(x, 25))
    
