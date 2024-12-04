"""Day 4"""

import numpy as np


day_4_file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_4/day_4_input_2.txt"


# get input from file
def read_file(file: str) -> list[str]:
    with open(file) as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from {file}")
    return lines


# use a vector
# find xmas in both horizontal and vertical directions and diagonally

# Read the file
lines = read_file(day_4_file)
array = np.array([list(line.strip()) for line in lines if line.strip()])


# Search for the string "XMAS" in various directions
def search_xmas(array: np.ndarray, target: str) -> list:
    positions = []
    target_len = len(target)
    rows, cols = array.shape

    # Search horizontally (forward and backward)
    for i in range(rows):
        for j in range(cols - target_len + 1):
            if "".join(array[i, j : j + target_len]) == target:
                positions.append((i, j, "forward"))
            if "".join(array[i, j : j + target_len][::-1]) == target:
                positions.append((i, j, "backward"))

    # Search vertically (down and up)
    for i in range(rows - target_len + 1):
        for j in range(cols):
            if "".join(array[i : i + target_len, j]) == target:
                positions.append((i, j, "down"))
            if "".join(array[i : i + target_len, j][::-1]) == target:
                positions.append((i, j, "up"))

    # Search diagonally (down-right and up-left)
    for i in range(rows - target_len + 1):
        for j in range(cols - target_len + 1):
            if "".join(array[i + k, j + k] for k in range(target_len)) == target:
                positions.append((i, j, "down-right"))
            if "".join(array[i + k, j + k] for k in range(target_len))[::-1] == target:
                positions.append((i, j, "up-left"))

    # Search diagonally (down-left and up-right)
    for i in range(rows - target_len + 1):
        for j in range(target_len - 1, cols):
            if "".join(array[i + k, j - k] for k in range(target_len)) == target:
                positions.append((i, j, "down-left"))
            if "".join(array[i + k, j - k] for k in range(target_len))[::-1] == target:
                positions.append((i, j, "up-right"))

    return positions


# Search for "XMAS"
positions = search_xmas(array, "XMAS")

print(f"Found 'XMAS': {len(positions)}")


# part 2.
# Search for the string "MAS" in various directions
def search_mas(array: np.ndarray, target: str) -> list:
    positions = []
    target_len = len(target)
    rows, cols = array.shape

    # Search diagonally (down-right and up-left)
    for i in range(rows - target_len + 1):
        for j in range(cols - target_len + 1):
            # Down-right diagonal search
            if "".join(array[i + k, j + k] for k in range(target_len)) == target:
                start = (i, j)
                end = (i + target_len - 1, j + target_len - 1)
                positions.append((start, end, "down-right"))

            # Up-left diagonal search
            if "".join(array[i + k, j + k] for k in range(target_len))[::-1] == target:
                start = (i + target_len - 1, j + target_len - 1)
                end = (i, j)
                positions.append((start, end, "up-left"))

    # Search diagonally (down-left and up-right)
    for i in range(rows - target_len + 1):
        for j in range(target_len - 1, cols):
            # Down-left diagonal search
            if "".join(array[i + k, j - k] for k in range(target_len)) == target:
                start = (i, j)
                end = (i + target_len - 1, j - target_len + 1)
                positions.append((start, end, "down-left"))

            # Up-right diagonal search
            if "".join(array[i + k, j - k] for k in range(target_len))[::-1] == target:
                start = (i + target_len - 1, j - target_len + 1)
                end = (i, j)
                positions.append((start, end, "up-right"))

    return positions


# Find intersections forming an 'X' pattern
def find_x_intersections(positions: list) -> list:
    intersections = []

    # Extract positions for each direction
    down_right_positions = [(start, end) for start, end, direction in positions if direction == "down-right"]
    up_left_positions = [(start, end) for start, end, direction in positions if direction == "up-left"]
    down_left_positions = [(start, end) for start, end, direction in positions if direction == "down-left"]
    up_right_positions = [(start, end) for start, end, direction in positions if direction == "up-right"]

    # Check for intersections between down-right and up-right vectors
    for dr_start, dr_end in down_right_positions:
        for ur_start, ur_end in up_right_positions:
            # Calculate the middle position of the down-right vector
            dr_middle = ((dr_start[0] + dr_end[0]) // 2, (dr_start[1] + dr_end[1]) // 2)
            # Calculate the middle position of the up-right vector
            ur_middle = ((ur_start[0] + ur_end[0]) // 2, (ur_start[1] + ur_end[1]) // 2)

            # Check if the middle positions intersect
            if dr_middle == ur_middle:
                intersections.append((dr_start, dr_end, ur_start, ur_end, "X"))

    # check for intersections between down-left and up-left vectors
    for dl_start, dl_end in down_left_positions:
        for ul_start, ul_end in up_left_positions:
            # Calculate the middle position of the down-left vector
            dl_middle = ((dl_start[0] + dl_end[0]) // 2, (dl_start[1] + dl_end[1]) // 2)
            # Calculate the middle position of the up-left vector
            ul_middle = ((ul_start[0] + ul_end[0]) // 2, (ul_start[1] + ul_end[1]) // 2)

            # Check if the middle positions intersect
            if dl_middle == ul_middle:
                intersections.append((dl_start, dl_end, ul_start, ul_end, "X"))

    # check for up-right and up-left intersections
    for ur_start, ur_end in up_right_positions:
        for ul_start, ul_end in up_left_positions:
            # Calculate the middle position of the up-right vector
            ur_middle = ((ur_start[0] + ur_end[0]) // 2, (ur_start[1] + ur_end[1]) // 2)
            # Calculate the middle position of the up-left vector
            ul_middle = ((ul_start[0] + ul_end[0]) // 2, (ul_start[1] + ul_end[1]) // 2)

            # Check if the middle positions intersect
            if ur_middle == ul_middle:
                intersections.append((ur_start, ur_end, ul_start, ul_end, "X"))

    # check for down-right and down-left intersections
    for dr_start, dr_end in down_right_positions:
        for dl_start, dl_end in down_left_positions:
            # Calculate the middle position of the down-right vector
            dr_middle = ((dr_start[0] + dr_end[0]) // 2, (dr_start[1] + dr_end[1]) // 2)
            # Calculate the middle position of the down-left vector
            dl_middle = ((dl_start[0] + dl_end[0]) // 2, (dl_start[1] + dl_end[1]) // 2)

            # Check if the middle positions intersect
            if dr_middle == dl_middle:
                intersections.append((dr_start, dr_end, dl_start, dl_end, "X"))

    return intersections


# Search for "MAS"
mas_positions = search_mas(array, "MAS")

# Find intersections forming an 'X' pattern
x_intersections = find_x_intersections(mas_positions)

print(f"Found 'MAS': {len(mas_positions)}")
print(f"Found 'X' intersections: {len(x_intersections)}")
