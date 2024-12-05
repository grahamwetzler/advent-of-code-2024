from collections import defaultdict
from functools import cmp_to_key
from pathlib import Path

rules_input, updates_input = (
    (Path(__file__).parent / Path("input.txt")).read_text().split("\n" * 2)
)

rules = defaultdict(list)
for rule in rules_input.splitlines():
    left, right = rule.split("|")
    rules[int(left)].append(int(right))

updates = [
    [int(page) for page in update.split(",")]
    for update in updates_input.strip().split("\n")
]


def page_is_correct(update, index, page):
    remaining = update[index + 1 :]
    return all([r in rules[page] for r in remaining])


def update_is_correct(update):
    update_valid = []
    for index, page in enumerate(update):
        is_correct = page_is_correct(update, index, page)
        update_valid.append(is_correct)

    if all(update_valid):
        return True

    return False


def split_updates(updates):
    correct = []
    incorrect = []
    for update in updates:
        if update_is_correct(update):
            correct.append(update)
        else:
            incorrect.append(update)

    return (correct, incorrect)


def sum_middle(updates):
    total = 0
    for update in updates:
        middle = int((len(update) - 1) / 2)
        total += update[middle]

    return total


def part_1(updates):
    return sum_middle(updates)


def part_2(updates):
    def custom_sort(a, b):
        if b in rules[a]:
            return -1
        elif a in rules[b]:
            return 1

        return 0

    correct = []
    for update in updates:
        sorted_numbers = sorted(update, key=cmp_to_key(custom_sort))
        correct.append(sorted_numbers)

    return sum_middle(correct)


if __name__ == "__main__":
    correct_updates, incorrect_updates = split_updates(updates)
    print("part 1:", part_1(correct_updates))
    print("part 2:", part_2(incorrect_updates))
