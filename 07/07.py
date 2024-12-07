import re
from copy import deepcopy
from itertools import product, zip_longest
from pathlib import Path
from time import time

input_text = (Path(__file__).parent / Path("input.txt")).read_text()

input = [
    [int(num) for num in re.split(":\s|\s", line)] for line in input_text.splitlines()
]


def handle_operation(num_1, num_2, operator):
    if operator == "||":
        return int(f"{num_1}{num_2}")

    return eval(f"{num_1} {operator} {num_2}")


def solve_line(line, calibration, operators):
    num_operators = len(line) - 1
    for operator_combination in product(operators, repeat=num_operators):
        equations = zip_longest(line, operator_combination)
        flattened_equations = [x for xs in equations for x in xs if x is not None]
        result = 0
        index = 3
        while flattened_equations:
            operate = flattened_equations[:index]
            del flattened_equations[:index]
            if len(operate) == 3:
                num_1, operator, num_2 = operate
                result += handle_operation(num_1, num_2, operator)
            else:
                operator, num_2 = operate
                result = handle_operation(result, num_2, operator)
            index = 2

        if result == calibration:
            return True

    return False


def solve_part(input, part):
    operators = {1: ("+", "*"), 2: ("+", "*", "||")}[part]
    start_time = time()
    calibration_total = 0
    for line in deepcopy(input):
        calibration = line.pop(0)
        if solve_line(line, calibration, operators):
            calibration_total += calibration
    total_time = time() - start_time

    print(f"took {total_time:.0f} seconds")
    return calibration_total


print("part 1:", solve_part(input, part=1))
print("part 2:", solve_part(input, part=2))
