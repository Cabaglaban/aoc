from functools import reduce

demo_in = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip().split("\n")


def find_a(idata, move_x=3, move_y=1):
    oidata = idata
    
    def extend(idata):
        return [r + oidata[idx] for idx, r in enumerate(idata)]
    
    x, y, t = 0, 0, 0

    while y < len(idata) - 1:
        x += move_x
        y += move_y
        
        if x >= len(idata[0]):
            idata = extend(idata)
        
        # print(x, y, idata[y], idata[y][x])
        try:
            if idata[y][x] == '#':
                t += 1
        except Exception as e:
            print(e)
            print(x, y, idata[y])
        
    return t

def find_b(idata):
    moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    
    results = []
    for move in moves:
        r = find_a(idata, *move)
        # print('for', move, '==', r)
        
        results.append(r)
        
    return reduce((lambda x, y: x * y), results)
        
    


print('a', find_a(demo_in))
print('b', find_b(demo_in))
print()
with open('in', 'r') as f:
    x = [r.strip() for r in f.readlines()]
    print('a', find_a(x))
    print('b', find_b(x))
    
