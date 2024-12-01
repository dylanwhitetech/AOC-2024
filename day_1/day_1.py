""" Day 1"""


# steps 
# take in 2 lists
# sort lists in ascending order

# from left list (first list)
# get the smallest number and second and third ....
# match smallest to smallest in right list
#match second smallest to second smallest in right list
# so on and so forth

# find total distance by adding up the differences between the matched numbers




file = "/Users/dyl13740/AdventofCode2024/AOC-2024/day_1/day_1_input_1.txt"


# get input from file
def read_file(file):
    with open(file) as f:
        lines = f.readlines()
        left_list = []
        right_list = []
        for line in lines:
            line = line.strip()
            line = line.split() # Split by any whitespace
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))
    return left_list, right_list



left_list, right_list = read_file(file)


print(left_list[0])
print(right_list[0])

# sort lists

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

# calculate total distance
total_distance = 0
for left, right in zip(sorted_left_list, sorted_right_list):
    total_distance += abs(left - right)

print("Total distance:", total_distance)


### Part 2
# how often does each number appear from left appear in right
# simliarity score = number multiplied by the number of times it appears in the right list
# total similarity score = sum of all similarity

lift_list_dict = {}
right_list_dict = {}

for left, right in zip(left_list, right_list):
    if left in lift_list_dict:
        lift_list_dict[left] += 1
    else:
        lift_list_dict[left] = 1

    if right in right_list_dict:
        right_list_dict[right] += 1
    else:
        right_list_dict[right] = 1

total_similarity_score = 0

for key in lift_list_dict:
    similarity_score = 0
    if key in right_list_dict:
        similarity_score = key * right_list_dict[key]
        total_similarity_score += similarity_score

print("Total similarity score:", total_similarity_score)