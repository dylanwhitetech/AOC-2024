"""Day 5"""

day_5_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_5/day_5_input_2.txt"
day_5_rules_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_5/day_5_input_rules.txt"


# get input from file
def read_file(file: str) -> list[str]:
    with open(file) as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from {file}")
    return lines


# lines to list of ints
def build_line(line: str) -> list[int]:
    line.strip()
    return [int(num) for num in line.split(",")]


# get all rules in list of tuple of ints
def build_ruleset(rules_source: list[str]) -> list[tuple[int, int]]:
    rules = []
    for rule in rules_source:
        rule = rule.strip()
        rules.append((int(rule.split("|")[0]), int(rule.split("|")[1])))

    return rules


def check_rule(rule: tuple[int, int], update_list: list[int]) -> tuple[list[int], bool]:
    first_index = 0
    second_index = 0

    # check rule first number
    if rule[0] in update_list and rule[1] in update_list:
        first_index = update_list.index(rule[0])
        # check rule second number
        second_index = update_list.index(rule[1])
    else:
        # do nothing
        return update_list, True

    # both numbers have been found
    if first_index < second_index:
        return update_list, True
    else:
        # insert the first index number before the second index number
        update_list.insert(first_index + 1, update_list.pop(second_index))
        return update_list, False


def get_middle_number(page_list: list[int]) -> int:
    # Ensure the list has an odd number of elements
    if len(page_list) % 2 == 0:
        raise ValueError("List must have an odd number of elements")

    # Find the middle index
    middle_index = len(page_list) // 2

    # Return the middle value
    return page_list[middle_index]


# read input and rules
day_5_input = read_file(day_5_file)
sorting_rules = read_file(day_5_rules_file)

# build the list of pages to update
update_list = []
for update in day_5_input:
    update_list.append(build_line(update.strip()))

# rules
rules = build_ruleset(sorting_rules)

# middle numbers
middle_numbers = []

# check the rules
for i in range(len(update_list)):
    correctly_ordered = True
    for rule in rules:
        update_list[i], correctly_ordered = check_rule(rule, update_list[i])
        if not correctly_ordered:
            break

    if correctly_ordered:
        middle_numbers.append(get_middle_number(update_list[i]))


# print(day_5_input)
# print(update_list)
# print(middle_numbers)
print(f"Part 1: {sum(middle_numbers)}")
print(len(middle_numbers))

## Part 2

update_list_part2 = []

for update in day_5_input:
    update_list_part2.append(build_line(update.strip()))


fixed_middle_numbers = []

for i in range(len(update_list_part2)):
    correctly_ordered = False

    loop_count = 0

    while not correctly_ordered:
        rule_results = []
        for rule in rules:
            update_list_part2[i], rule_result = check_rule(rule, update_list_part2[i])
            rule_results.append(rule_result)

        # Check if all rule results are True
        if all(rule_results):
            correctly_ordered = True

        loop_count += 1

    if correctly_ordered and loop_count > 1:
        fixed_middle_numbers.append(get_middle_number(update_list_part2[i]))

# print(update_list_part2)

# print(fixed_middle_numbers)
print(f"Part 2: {sum(fixed_middle_numbers)}")
