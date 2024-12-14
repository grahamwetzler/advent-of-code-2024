import re
from copy import deepcopy
from itertools import product, zip_longest
from pathlib import Path

input_text = (Path(__file__).parent / Path("input.txt")).read_text()

input = [
    [int(num) for num in re.split(":\s|\s", line)] for line in input_text.splitlines()
]


def solve_line(line, calibration, operators):
    ops = {
        "*": lambda a, b: a * b,
        "+": lambda a, b: a + b,
        "||": lambda a, b: int(f"{a}{b}"),
    }
    num_operators = len(line) - 1
    for operator_combination in product(operators, repeat=num_operators):
        equations = zip_longest(line, operator_combination)
        flattened_equations = [x for xs in equations for x in xs if x is not None]
        result = 0
        index = 3
        while flattened_equations:
            operate = [flattened_equations.pop(0) for _ in range(index)]
            if len(operate) == 3:
                num_1, operator, num_2 = operate
                result += ops[operator](num_1, num_2)
            else:
                operator, num_2 = operate
                result = ops[operator](result, num_2)
            index = 2

        if result == calibration:
            return True

    return False


def solve_part(input, part):
    operators = {1: ("+", "*"), 2: ("+", "*", "||")}[part]
    calibration_total = 0
    for line in deepcopy(input):
        calibration = line.pop(0)
        if solve_line(line, calibration, operators):
            calibration_total += calibration

    return calibration_total


print("part 1:", solve_part(input, part=1))
print("part 2:", solve_part(input, part=2))
