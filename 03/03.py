import re
from pathlib import Path

input = Path("03/03.txt").read_text()


def part_1(input):
    instructions = re.findall("mul\((\d*,\d*)\)", input)

    total = 0
    for instruction in instructions:
        num_1, num_2 = instruction.split(",")
        total += int(num_1) * int(num_2)

    return total


def part_2(input):
    instructions = re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", input)

    total = 0
    do = True
    for instruction in instructions:
        if instruction == "don't()":
            do = False
        elif instruction == "do()":
            do = True
            continue

        if not do:
            continue

        num_1, num_2 = instruction[4:][:-1].split(",")
        total += int(num_1) * int(num_2)

    return total


assert part_1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161  # fmt: off
assert part_2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48  # fmt: off

print("part 1:", part_1(input))
print("part 2:", part_2(input))
