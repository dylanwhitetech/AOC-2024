"""Day 3"""

import re


day_3_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_3/day_3_input_2.txt"


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


# print(f"Part 2: {enable} {disable}")

# Regular expression to match mul(some_number, some_number), do(), and don't() using non-capturing groups for do() and don't()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"
# pattern = r"do\(\)"

all_matches = []

for line in day_3_input:
    matches = re.findall(pattern, line)
    for match in matches:
        if match[0] and match[1]:  # mul(some_number, some_number)
            all_matches.append((int(match[0]), int(match[1])))
        elif match[2]:  # do()
            all_matches.append(match[2])
        elif match[3]:  # don't()
            all_matches.append(match[3])

results = 0
enable = True

for instruction in all_matches:
    if instruction == "do()":
        enable = True
    elif instruction == "don't()":
        enable = False
    elif enable:
        results += instruction[0] * instruction[1]
    else:
        print(f"shits broke: {instruction}")

print(f"Part 2: {results}")
