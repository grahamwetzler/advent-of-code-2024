from util import get_input

input = get_input().splitlines()
input_parsed = [[int(level) for level in report.split(" ")] for report in input]


def is_safe(report):
    differences = []
    for idx, level in enumerate(report):
        if idx == 0:
            continue
        differences.append(level - report[idx - 1])

    return all(
        [
            any(
                [
                    all([difference < 0 for difference in differences]),
                    all([difference > 0 for difference in differences]),
                ]
            ),
            all([1 <= abs(difference) <= 3 for difference in differences]),
        ]
    )


print("part 1:", sum([is_safe(report) for report in input_parsed]))


def all_possibilities(report):
    possibilities = []
    for idx in range(len(report)):
        possibility = report.copy()
        possibility.pop(idx)
        possibilities.append(possibility)

    return possibilities


part_2 = []
for report in input_parsed:
    possibilities = all_possibilities(report)
    scenario = []

    for possibility in possibilities:
        scenario.append(is_safe(possibility))

    part_2.append(any(scenario))

print("part 2:", sum(part_2))
