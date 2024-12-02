"""Day 2"""

# from aoc_utils import read_file

from aoc_utils import read_file, all_values_same, one_bad_level, test_report, check_for_duplicate

day_2_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_2/day_2_input_1.txt"

day_2_input = read_file(day_2_file)

# all lines are read.
# print(day_2_input[0])  # 19 21 24 27 24

# each list is a report
# reports are safe if gradually decreasing or increasing
# increase or decrease by 1 or 2 or 3
# only increasing or decreasing


safe_reports = 0

for report in day_2_input:
    report = report.split()
    report = [int(x) for x in report]
    # print(report)

    is_safe, report_check = test_report(report)

    if check_for_duplicate(report_check, report):
        # print(report)
        print(report_check)
        # safe_reports += 1
    elif is_safe and all_values_same(report_check):
        # print(report_check)
        safe_reports += 1
    # elif is_safe and one_bad_level(report_check, report):
    #     # print(report_check)
    #     safe_reports += 1

print(f"Safe reports: {safe_reports}")
