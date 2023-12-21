from aoc.utils import *
from math import lcm
from functools import partial


class Module:
    BROADCASTER = "b"
    FLIP_FLOP = "%"
    CONJUNCTION = "&"
    RX = "rx"


def parse_line(line: str):
    name, outputs = split_strip(line, " -> ")
    return (name[1:] if name[0] in "%&" else name, name[0], split_strip(outputs, ","))


def sort_modules(modules):
    modules[Module.RX] = [Module.CONJUNCTION, []]

    flip_flops = {}
    conjunctions = {}

    for name, m in modules.items():
        t, o = m
        if t == Module.FLIP_FLOP:
            flip_flops[name] = 0
        for oname in o:
            if modules[oname][0] == Module.CONJUNCTION:
                conjunctions.setdefault(oname, {})[name] = -1 if oname == Module.RX else 0

    return flip_flops, conjunctions


def solve(modules, solve_rx):
    flip_flops, conjunctions = sort_modules(modules)
    count = [0, 0]
    p = 0

    # rx <- [..] <- [.., .., ..]
    rx_input = conjunctions.get(Module.RX, {}).keys()
    if not rx_input:
        rx = None
    else:
        assert len(rx_input) == 1
        rx_parent = list(conjunctions["rx"].keys())[0]
        rx = {k: 0 for k in conjunctions[rx_parent].keys()}

    while True:
        p += 1
        queue = [("button", "broadcaster", 0)]
        if p == 1000 and not solve_rx:
            return count[0] * count[1]

        if rx and all(rx.values()):
            return lcm(*rx.values())

        while queue:
            src, module, pulse = queue.pop(0)
            count[pulse] += 1

            mtype, outputs = modules[module]
            match mtype, pulse:
                case Module.BROADCASTER, _:
                    pass
                case Module.FLIP_FLOP, 0:  # only low pulse for flip flops
                    pulse = flip_flops[module] = not flip_flops[module]
                case Module.CONJUNCTION, _:
                    conjunctions[module][src] = pulse
                    pulse = 0 if all(conjunctions[module].values()) else 1
                    if rx and pulse and module in rx and not rx[module]:
                        rx[module] = p
                case _:
                    continue

            for o in outputs:
                queue.append((module, o, pulse))


for ex, p, solver in generate_runs(args=[[("P1", solve), ("P2", solve)]]):
    modules = {k: v for k, *v in read_day_input(ex, line_parser=parse_line)}
    solver = partial(solve, solve_rx=(p=="P2" and not ex))
    print(f"[{p}][ex={int(ex)}] ", solver(modules))
