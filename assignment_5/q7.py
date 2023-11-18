from collections import Counter
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):

    top_dict = {index: item for index, item in enumerate(top)}
    btm_dict = {index: item for index, item in enumerate(bottom)}
    # print(top_dict)
    # print(btm_dict)

    combined_dict = {}
    for key in top_dict.keys() | btm_dict.keys():
        combined_dict[key] = [top_dict.get(key, None), btm_dict.get(key, None)]
    common_numbers = set(combined_dict[0])
    for key in combined_dict:
        common_numbers = common_numbers.intersection(set(combined_dict[key]))
    # Check if it's possible to complete or not
    if len(common_numbers) == 0:
        return -1
    common_number_list = []
    for element in common_numbers:
        common_number_list.append(element)

    temp_lists = [0] * len(common_number_list)
    for number in common_number_list:
        index = 0
        for value in top_dict.values():
            if value != number:
                temp_lists[index] += 1
        index += 1

    temp2_lists = [0] * len(common_number_list)
    for number in common_number_list:
        index = 0
        for value in btm_dict.values():
            if value != number:
                temp2_lists[index] += 1
        index += 1

    # print(temp_lists)
    # print(temp2_lists)

    combined_list = temp_lists + temp2_lists
    answer = min(combined_list)
    
    return answer

# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))

# [2, 6, 2, 1, 2, 2]
# [5, 2, 4, 2, 3, 2]