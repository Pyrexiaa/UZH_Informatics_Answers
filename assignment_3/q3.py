import re

def is_valid(password):
    # Implement this function
    if not (8 <= len(password) <= 16):
        return False

    if not re.match(r'^[a-zA-Z0-9+\-*/]+$', password):
        return False

    if len(re.findall(r'[a-z]', password)) < 2:
        return False

    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    if len(re.findall(r'\d', password)) < 2:
        return False

    if len(re.findall(r'[+\-*/]', password)) < 2:
        return False

    # Make sure you return the correct result at the end!
    return True

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid("abAB12+-"))

