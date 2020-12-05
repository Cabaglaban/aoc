from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')

def find_from_expr(expr, data_range):
    for ch in expr:
        r = (data_range[1] - data_range[0]) // 2 + 1
        if ch in ['F', 'L']:
            data_range = (data_range[0], data_range[1] - r)
        elif ch in ['B', 'R']:
            data_range = (data_range[0] + r, data_range[1])
        
    return min(data_range)

def find_a(idata):
    r = find_from_expr(idata[:7], (0, 127))
    c = find_from_expr(idata[7:], (0, 7))
    
    # print(idata, r, c)
    return r * 8 + c

def find_b(idata):
    ids = {find_a(i) for i in idata}
    full_ids = {x for x in range(min(ids), max(ids))}
    
    return full_ids - ids
    
    


assert find_a("FBFBBFFRLR") == 357
assert find_a("BFFFBBFRRR") == 567
assert find_a("FFFBBBFRRR") == 119
assert find_a("BBFFBBFRLL") == 820
print()
with open(in_file, 'r') as f:
    x = [r.strip() for r in f.readlines()]
    m = 0
    for item in x:
        m = max(m, find_a(item))
    print('a', m)

    print('b', find_b(x))
    
