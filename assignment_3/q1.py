# Determine the right size of a shirt. Change the function
# below to determine the right size of a shirt.
# Your implementation should work with any specific value.

def get_size(circumference):
    size = "N/A"
    # your code here
    if 80 <= circumference <= 90:
        size = "XS"
    elif 90 < circumference <= 98:
        size = "S"
    elif 98 < circumference <= 104:
        size = "M"
    elif 104 < circumference <= 111:
        size = "L"
    elif 111 < circumference <= 124:
        size = "XL"
    # don't forget to return the computed value!
    return size

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_size(111))
