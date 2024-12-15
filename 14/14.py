import re
from itertools import count, groupby, product
from math import prod
from pathlib import Path

test_input = [
    [int(n) for n in re.findall("-?\d+", r)]
    for r in (Path(__file__).stem / Path("test_input.txt")).read_text().splitlines()
]
input = [
    [int(n) for n in re.findall("-?\d+", r)]
    for r in (Path(__file__).stem / Path("input.txt")).read_text().splitlines()
]


def part_1(input, width, height, seconds):
    final = {(x, y): 0 for x, y in product(range(width), range(height))}
    quadrants = dict(tl=0, tr=0, bl=0, br=0)
    left = range(0, width // 2)
    right = range(width // 2 + 1, width)
    top = range(0, height // 2)
    bottom = range(height // 2 + 1, height)

    for robot in input:
        x, y, vx, vy = robot
        x = (x + vx * seconds) % width
        y = (y + vy * seconds) % height
        final[(x, y)] += 1

        if y in top and x in left:
            quadrants["tl"] += 1
        elif y in top and x in right:
            quadrants["tr"] += 1
        elif y in bottom and x in left:
            quadrants["bl"] += 1
        elif y in bottom and x in right:
            quadrants["br"] += 1

    return prod(quadrants.values())


def part_2(input, width, height):
    for seconds in count():
        final = {(x, y): 0 for x, y in product(range(width), range(height))}

        for robot in input:
            x, y, vx, vy = robot
            x = (x + vx * seconds) % width
            y = (y + vy * seconds) % height
            if final[(x, y)] > 1:
                break
            final[(x, y)] += 1

        max_continuous_group = max(
            [len(list(g)) for k, g in groupby(final.values()) if k > 0]
        )
        if max_continuous_group > 10:
            break

    print("part 2:", seconds)
    print(
        "\n".join(
            [
                "".join(["#" if final[(x, y)] > 0 else " " for x in range(width)])
                for y in range(height)
            ]
        )
    )


assert part_1(test_input, width=11, height=7, seconds=100) == 12
print("part 1:", part_1(input, width=101, height=103, seconds=100))
part_2(input, width=101, height=103)
