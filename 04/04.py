import itertools
from pathlib import Path


def parse_input(input: str):
    return [[col for col in row] for row in input.splitlines()]


def part_1(input):
    def count_xmas(characters):
        xmas = "XMAS"
        length = len(characters)
        xmas_count = 0
        for index in range(length):
            joined_characters = "".join(characters[index : index + len(xmas)])
            if joined_characters in (xmas, xmas[::-1]):
                xmas_count += 1

        return xmas_count

    width = len(input[0])
    height = len(input)
    columns = [[] for _ in range(width)]
    rows = [[] for _ in range(height)]
    forwards_diagonal = [[] for _ in range(height + width - 1)]
    backwards_diagonal = [[] for _ in range(len(forwards_diagonal))]
    min_backwards_diagonal = -height + 1

    for x, y in itertools.product(range(width), range(height)):
        columns[x].append(input[y][x])
        rows[y].append(input[y][x])
        forwards_diagonal[x + y].append(input[y][x])
        backwards_diagonal[x - y - min_backwards_diagonal].append(input[y][x])

    return sum(
        [count_xmas(col) for col in columns]
        + [count_xmas(row) for row in rows]
        + [count_xmas(diagonal) for diagonal in forwards_diagonal]
        + [count_xmas(diagonal) for diagonal in backwards_diagonal]
    )


def part_2(input):
    width = len(input)
    height = len(input[0])
    blocks = []
    for row_idx, col_idx in itertools.product(range(height), range(width)):
        block = [
            row[col_idx - 1 : col_idx + 2] for row in input[row_idx - 1 : row_idx + 2]
        ]
        if len(block) < 3 or len(block[0]) < 3:
            continue

        if block[1][1] == "A":
            blocks.append(block)

    total = 0
    for block in blocks:
        if (  # top left to bottom right
            (block[0][0] == "M" and block[2][2] == "S")
            or (block[0][0] == "S" and block[2][2] == "M")
        ) and (  # bottom left to top right
            (block[2][0] == "M" and block[0][2] == "S")
            or (block[2][0] == "S" and block[0][2] == "M")
        ):
            total += 1

    return total


test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test_input_parsed = parse_input(test_input)
assert part_1(test_input_parsed) == 18
assert part_2(test_input_parsed) == 9


input = Path("04/input.txt").read_text()
parsed_input = parse_input(input)
print("part 1:", part_1(parsed_input))
print("part 2:", part_2(parsed_input))
