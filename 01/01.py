from pathlib import Path

input = [int(n) for n in Path("01/01.txt").read_text().split()]
left_ids = sorted(input[::2])
right_ids = sorted(input[1::2])

part_1 = sum([abs(left - right) for left, right in zip(left_ids, right_ids)])

print("part 1: ", part_1)

part_2 = sum([left * right_ids.count(left) for left in left_ids])

print("part 2: ", part_2)
