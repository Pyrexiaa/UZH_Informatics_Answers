# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    if not isinstance(d, dict):
        print("We only accept dictionary!")
        return None

    inverted_dict = {}
    
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    
    for key in inverted_dict:
        inverted_dict[key].sort()
    
    return inverted_dict


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
