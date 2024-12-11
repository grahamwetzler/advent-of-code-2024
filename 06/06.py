from collections import namedtuple
from copy import deepcopy
from pathlib import Path

input_text = (Path(__file__).parent / Path("input.txt")).read_text()
input = [[col for col in row] for row in input_text.splitlines()]


step = namedtuple("step", ["row", "col", "approach_direction"])


class InfiniteLoopError(Exception): ...


class OffMapError(Exception): ...


def get_start(input):
    for row_index, row in enumerate(input):
        for col_index, col in enumerate(row):
            if col == "^":
                return (row_index, col_index)


def move_guard(input, row, col, direction):
    movement = {
        "^": lambda row, col: (row - 1, col),
        ">": lambda row, col: (row, col + 1),
        "v": lambda row, col: (row + 1, col),
        "<": lambda row, col: (row, col - 1),
    }
    next_row, next_col = movement[direction](row, col)

    if next_row not in range(len(input)) or next_col not in range(len(input[0])):
        raise OffMapError

    next_step = input[next_row][next_col]

    if next_step == "#":
        turn = {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^",
        }
        return row, col, turn[direction]

    return next_row, next_col, direction


def patrol(input, row, col):
    visited = set()
    direction = "^"
    while True:
        this_step = step(row=row, col=col, approach_direction=direction)
        if this_step in visited:
            raise InfiniteLoopError

        visited.add(this_step)

        try:
            row, col, direction = move_guard(input, row, col, direction)
        except OffMapError:
            break

    return visited


def part_2():
    blocks = set()
    for row, col in visited_coordinates:
        input_copy = deepcopy(input)
        input_copy[row][col] = "#"
        try:
            patrol(input_copy, start_row, start_col)
        except InfiniteLoopError:
            blocks.add((row, col))

    return len(blocks)


start_row, start_col = get_start(input)
part_1_visited = patrol(input=input, row=start_row, col=start_col)
visited_coordinates = {(d.row, d.col) for d in part_1_visited}
print("part 1:", len(visited_coordinates))
print("part 2:", part_2())
