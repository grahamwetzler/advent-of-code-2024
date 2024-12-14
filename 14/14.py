import re
from math import prod
from pathlib import Path
from pprint import pprint

test_input = [
    [int(n) for n in re.findall("-?\d+", r)]
    for r in (Path(__file__).stem / Path("test_input.txt")).read_text().splitlines()
]
input = [
    [int(n) for n in re.findall("-?\d+", r)]
    for r in (Path(__file__).stem / Path("input.txt")).read_text().splitlines()
]


def simulate(input, width, height, seconds):
    final = []
    for robot in input:
        x, y, vx, vy = robot
        x = (x + vx * seconds) % width
        y = (y + vy * seconds) % height
        final.append((x, y))

    f = dict(tl=0, tr=0, bl=0, br=0)
    left = range(0, width // 2)
    right = range(width // 2 + 1, width)
    top = range(0, height // 2)
    bottom = range(height // 2 + 1, height)

    for pos in final:
        x, y = pos
        if y in top and x in left:
            f["tl"] += 1
        elif y in top and x in right:
            f["tr"] += 1
        elif y in bottom and x in left:
            f["bl"] += 1
        elif y in bottom and x in right:
            f["br"] += 1

    return prod(f.values())


assert simulate(test_input, width=11, height=7, seconds=100) == 12
print(simulate(input, width=101, height=103, seconds=100))
