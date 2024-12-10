# type: ignore
from itertools import zip_longest
from pathlib import Path
from pprint import pprint  # noqa

input_text = (Path(__file__).parent / Path("input.txt")).read_text()
# input_text = (Path(__file__).parent / Path("test_input.txt")).read_text()
input = [int(n) for n in input_text.strip()]


def flatten(arg):
    if not isinstance(arg, (list, tuple)):
        return [arg]
    return [x for sub in arg for x in flatten(sub) if x is not None]


du = [[i] * n for i, n in enumerate(input[0::2])]
fs = [["."] * n for n in input[1::2]]
zipped = zip_longest(du, fs)
blocks = flatten(list(zipped))

# print("".join([str(b) for b in blocks]))
ids = list(set([b for b in blocks if b != "."]))


def blocks_sorted(blocks):
    if all([b == "." for b in blocks[-blocks.count(".") :]]):
        return True

    return False


# iterations = 0
last_idx_checked = 0
while not blocks_sorted(blocks):
    for idx, val in enumerate(blocks[:last_idx_checked:-1], start=last_idx_checked + 1):
        if val != ".":
            value_idx = len(blocks) - idx
            break

    value = blocks.pop(value_idx)
    fs_idx = blocks.index(".")
    blocks[fs_idx] = value
    blocks.append(".")

    # print(f"{iterations} / {len(blocks)}")
    # iterations += 1
    # print("".join([str(b) for b in blocks]))

# print("".join([str(b) for b in mb]))
print(sum([ids.index(f) * i for i, f in enumerate(blocks) if f != "."]))

# 15739685727547 too high
