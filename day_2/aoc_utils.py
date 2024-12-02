"""Utils for Advent of Code 2024."""


# get input from file
def read_file(file: str) -> list[str]:
    with open(file) as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from {file}")
    return lines


def test_report(report: list[int]) -> tuple[bool, list[str]]:
    increasing_or_decreasing = []
    is_safe = False

    for i in range(0, len(report) - 1):
        level_difference = report[i] - report[i + 1]

        if level_difference > 0 and abs(level_difference) <= 3:
            increasing_or_decreasing.append("decreasing")
            is_safe = True
        elif level_difference < 0 and abs(level_difference) <= 3:
            increasing_or_decreasing.append("increasing")
            is_safe = True
        elif level_difference == 0:
            increasing_or_decreasing.append("duplicate")
            is_safe = False
        else:
            is_safe = False
            break

    return is_safe, increasing_or_decreasing


def all_values_same(list: list) -> bool:
    for result in list:
        if result != list[0]:
            return False
    return True


def one_bad_level(list: list[str], report: list[int]) -> bool:
    increasing = "increasing"
    decreasing = "decreasing"
    increasing_count = 0
    decreasing_count = 0

    for result in list:
        if result == increasing:
            increasing_count += 1

        if result == decreasing:
            decreasing_count += 1

    if increasing_count == 1:
        index = list.index(increasing)
        new_report = report.copy()
        del new_report[index + 1]
        is_safe, report_check = test_report(report)
        if is_safe and all_values_same(report_check):
            return True

    elif decreasing_count == 1:
        index = list.index(decreasing)
        new_report = report.copy()
        del new_report[index + 1]
        is_safe, report_check = test_report(new_report)
        if is_safe and all_values_same(report_check):
            return True

    return False


def check_for_duplicate(list: list[str], report: list[int]) -> bool:
    duplicate = "duplicate"
    duplicate_count = 0

    for result in list:
        if result == duplicate:
            duplicate_count += 1

    if duplicate_count == 1:
        index = list.index(duplicate)
        new_report = report.copy()
        del new_report[index + 1]
        is_safe, report_check = test_report(new_report)
        if is_safe and all_values_same(report_check):
            return True

    return False
