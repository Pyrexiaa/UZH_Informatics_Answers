# perform the transformation
def transform_string(s):
    # Insert your code here.
    # Maybe you will want to use a temporary variable to hold the index
    # of the ":" character, so you can use it afterwards to slice the string?
    index = s.find(":")
    infront = s[:index]
    infront = infront.lower()
    behind = s[index:]
    behind = behind.upper()
    result = infront + behind
    return result

# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string("aB:cD"))