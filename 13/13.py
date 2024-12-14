import re
from collections import namedtuple
from pathlib import Path

machine = namedtuple("machine", ("ax", "ay", "bx", "by", "x", "y"))
input = (Path(__file__).parent / Path("input.txt")).read_text().split("\n" * 2)
machines = [machine(*[int(n) for n in re.findall("\d+", m)]) for m in input]


def solve(machines, offset=0):
    coins = 0
    for machine in machines:
        ax, ay, bx, by, x, y = machine
        d = ax * by - bx * ay
        da = bx * (y + offset) - (x + offset) * by
        db = ax * (y + offset) - (x + offset) * ay
        a = abs(da / d)
        b = abs(db / d)
        if all([a.is_integer(), b.is_integer()]):
            coins += int(a * 3 + b)

    return coins


print("part 1:", solve(machines))
print("part 2:", solve(machines, offset=1e13))
