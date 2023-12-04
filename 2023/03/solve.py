INPUT_FILE = "example"
INPUT_FILE = "input"


def parse_line(line: str):
    return line


with open(INPUT_FILE) as f:
    input = [parse_line(l.strip()) for l in f.readlines()]

line_length = len(input[0])


def has_adjacent_symbol(x, y):
    gear_pos = []
    has_symbol = False

    for ax, ay in [
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
    ]:
        try:
            if ax < 0 or ay < 0:
                raise IndexError
            
            val = input[ay][ax]
            if val == "*":
                gear_pos.append((ay, ax))
            if val != "." and not val.isnumeric():
                has_symbol = True
        except IndexError:
            pass

    return has_symbol, gear_pos


total = 0
valid_numbers = []
gears = {}

for y, line in enumerate(input):
    number = ""
    number_gear = []
    adjacent_symbol = False
    for x, c in enumerate(line):
        # print(f"{c} @ {x}.{y}; {number=}; {adjacent_symbol=}\n")
        if c.isnumeric():
            number += c
            cur_adjacent_symbol, g = has_adjacent_symbol(x, y)
            number_gear.extend(g)
            if cur_adjacent_symbol:
                adjacent_symbol = True
        else:
            if len(number) and adjacent_symbol:
                valid_numbers.append(int(number))
                for g in number_gear:
                    gears.setdefault(g, set()).add(int(number))

            number = ""
            number_gear = []
            adjacent_symbol = False

    if len(number) and adjacent_symbol:
        valid_numbers.append(int(number))
        for g in number_gear:
            gears.setdefault(g, set()).add(int(number))

# part 1
print(sum(valid_numbers))

# part 2
ratios = 0
for gear_numbers in gears.values():
    if len(gear_numbers) == 2:
        a, b = tuple(gear_numbers)
        ratios += a * b
print(ratios)
