from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')


demo_in = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


def find_a(idata, raw=True):
    if raw:
        instrs = [i.strip().split(' ') for i in idata.split('\n')]
    else:
        instrs = idata
    acc = 0
    visited = []

    idx = 0
    while idx < len(instrs):
        if idx in visited:
            # print('already been at', idx, 'acc is', acc)
            return acc, False
        visited.append(idx)

        op, n = instrs[idx][0], int(instrs[idx][1])
        if op == 'nop':
            pass
        elif op == 'acc':
            acc += n
        elif op == 'jmp':
            idx += n
            continue
        idx += 1
    return acc, True


def find_b(idata):
    instrs = [i.strip().split(' ') for i in idata.split('\n')]

    for idx, i in enumerate(instrs):
        op, n = instrs[idx][0], int(instrs[idx][1])
        next_op = 'jmp' if op == 'nop' else 'nop'

        copy = [i for i in instrs]
        copy[idx] = [next_op, n]
        # print(f'trying with {copy[idx]} at {idx}')

        acc, success = find_a(copy, False)
        if success:
            return acc

print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
    
