"""Day 3"""

import re


day_3_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_3/day_3_input_1.txt"


# multiply numbers that are stored in memory
# but its corrupted
# get combination of "mul(some_number, some_number)" in every occurance in each line
# mul(#, #) is to multiply two numbers
# add up the results of all multiplication operations


# get input from file
def read_file(file: str) -> list[str]:
    with open(file) as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from {file}")
    return lines


day_3_input = read_file(day_3_file)

# Regular expression to match mul(some_number, some_number)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

# Find all matches in the input string
for line in day_3_input:
    matches = re.findall(pattern, line)

    # Convert the results to int
    int_matches = [(int(x), int(y)) for x, y in matches]
    # print(int_matches)

    # Loop through the list and extract numbers
    numbers = []

    for pair in int_matches:
        numbers.append(pair[0] * pair[1])

    for n in numbers:
        total += n


print(f"Part 1: {total}")

