"""Day 6"""

import numpy as np

day_6_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_6/day_6_input_1.txt"


# get input from file


def read_file_to_array(filename: str) -> np.ndarray:
    with open(filename, "r") as file:
        lines = [list(line.strip()) for line in file]
    return np.array(lines)


lab_layout = read_file_to_array(day_6_file)
# print(lab_layout)

# get field of view
# Get the number of columns in the array
num_columns = lab_layout.shape[1]
num_rows = lab_layout.shape[0]

guard_options = [["^", "up"], [">", "right"], ["v", "down"], ["<", "left"]]


def get_guard_location_direction(input_array: np.ndarray, guard_options: list[list]) -> tuple:
    for config in guard_options:
        guard_location = np.where(input_array == config[0])

        if guard_location[0].size > 0:  # Check if the guard is found
            location = (int(guard_location[0][0]), int(guard_location[1][0]))
            direction = config

            print(f"Guard location: {location} | {direction}")
            return location, direction

    return None, None


# part 1
def move_guard(lab_layout: np.ndarray, guard_info: tuple, guard_options: list[list]) -> tuple:
    location, direction = guard_info
    icon, facing = direction

    # Define movement directions
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

    # Get the movement delta based on the current facing direction
    delta = directions[facing]

    # Calculate the new location
    new_location = (location[0] + delta[0], location[1] + delta[1])

    # Check if the new location is within bounds and not an obstacle
    if 0 <= new_location[0] < lab_layout.shape[0] and 0 <= new_location[1] < lab_layout.shape[1]:
        if lab_layout[new_location] != "#":
            # Move to the new location
            # lab_layout[location] = "X"
            lab_layout[new_location] = icon

            return (new_location, direction), lab_layout
        else:
            # Turn right to the next direction in guard_options
            current_index = next(i for i, option in enumerate(guard_options) if option[1] == facing)
            new_facing = guard_options[(current_index + 1) % len(guard_options)]

            return (location, new_facing), lab_layout
    else:
        # new location will be ouside the lab.
        # lab_layout[location] = "X"
        return (new_location, direction), lab_layout


def guard_in_lab_check(lab_layout: np.ndarray, guard_info: tuple) -> bool:
    guard_row, guard_col = guard_info[0]
    lab_rows, lab_columns = lab_layout.shape
    if 0 <= guard_row < lab_rows and 0 <= guard_col < lab_columns:
        return True
    return False


def loop_check(lab_layout: np.ndarray, guard_info: tuple, guard_options: list[list]) -> bool:
    # current location and direction
    initial_location, initial_direction = guard_info
    icon, facing = initial_direction

    # Define movement directions
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

    # Turn right to the next direction in guard_options
    current_index = next(i for i, option in enumerate(guard_options) if option[1] == facing)
    new_direction = guard_options[(current_index + 1) % len(guard_options)]
    guard_info = (initial_location, new_direction)

    # Move the guard and check if it returns to the initial position and direction
    while guard_in_lab_check(lab_layout, guard_info):
        guard_info, lab_layout = move_guard(lab_layout, guard_info, guard_options)

        # current location
        guard_row, guard_col = guard_info[0]
        

        if guard_info[0] == initial_location and guard_info[1] == initial_direction:
            return True

    return False


# part 2 cont.


# as guard is moving, check if he turns right, will he loop back to the same location following the same move rules
# if yes, then the guard is in a loop
# count the number of possible loops
# note if the guards current location produces a loop as he turns. then track the location a new obstacle that would produce the loop

starting_guard_info = get_guard_location_direction(lab_layout, guard_options)

guard_info = starting_guard_info  # ((6, 4), ['^', 'up'])
current_direction = starting_guard_info[1][1]
current_position = starting_guard_info[0]

loop_count = 0

while guard_in_lab_check(lab_layout, guard_info):
    if loop_check(lab_layout, guard_info, guard_options):
        loop_count += 1
        print(f"Loop count: {loop_count}")

    guard_info, lab_layout = move_guard(lab_layout, guard_info, guard_options)
    print(f"moved to: {guard_info[0]}")


print(f"Final Guard location: {guard_info[0]} | {guard_info[1]}")
print(f"Loop count: {loop_count}")
