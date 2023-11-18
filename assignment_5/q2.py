#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    if not a or not b:
        return []
    
    merged_list = []
    min_length = min(len(a), len(b))

    for i in range(min_length):
        merged_list.append((a[i], b[i]))

    if len(a) > len(b):
        for i in range(len(b), len(a)):
            merged_list.append((a[i], b[-1]))
    elif len(b) > len(a):
        for i in range(len(a), len(b)):
            merged_list.append((a[-1], b[i]))

    return merged_list



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
