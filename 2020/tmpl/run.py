from functools import reduce
import os

in_file = os.path.join(os.path.dirname(__file__), 'in')


demo_in = """
""".strip()


def find_a(idata):
    pass

def find_b(idata):
    pass
    


print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open(in_file, 'r') as f:
    x = f.read().strip()
    print('a', find_a(x))
    print('b', find_b(x))
    
