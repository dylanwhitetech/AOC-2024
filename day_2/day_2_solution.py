from aoc_utils import read_file

day_2_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_2/day_2_input_1.txt"

day_2_input = read_file(day_2_file)


def part1() -> None:
    num_safe_reports = 0
    for report in day_2_input:
        report = list(map(int, report.split(" ")))

        ascending = True if report[1] - report[0] > 0 else False
        for i in range(0, len(report) - 1):
            difference = report[i + 1] - report[i]
            if not 1 <= abs(difference) <= 3:
                break  # move to next report (continue outer loop)
            if (ascending and difference < 0) or (not ascending and difference > 0):
                break

            if i == len(report) - 2:
                num_safe_reports += 1

    print("Part 1:", num_safe_reports)


def part2() -> None:
    def is_safe(report: list[int]) -> bool:
        ascending = report[1] > report[0]
        for i in range(1, len(report)):
            difference = report[i] - report[i - 1]
            if not (1 <= abs(difference) <= 3):
                return False
            elif (ascending and difference < 0) or (not ascending and difference > 0):
                return False
        return True

    num_safe_reports = 0
    for report in day_2_input:
        report = list(map(int, report.split(" ")))

        if is_safe(report):
            num_safe_reports += 1
            continue

        # apply problem dampener
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]  # loops through report removing each value and testing new iteration
            if is_safe(modified_report):
                num_safe_reports += 1
                break

    print("Part 2:", num_safe_reports)


part1()
part2()
