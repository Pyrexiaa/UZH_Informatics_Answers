# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def sort(iterable):
    # Check if the input is None or non-iterable
    if iterable is None or not hasattr(iterable, '__iter__'):
        return None
    
    # Create a new list with the sorted elements
    sorted_list = sorted(iterable)
    
    return sorted_list

if __name__ == "__main__":
    numbers = [4, 2, 7, 1, 9, 5]
    sorted_numbers = sort(numbers)
    print("Original list:", numbers)
    print("Sorted list:", sorted_numbers)

    words = ('apple', 'orange', 'banana', 'grape', 'cherry')
    sorted_words = sort(words)
    print("Original tuple:", words)
    print("Sorted tuple:", sorted_words)

    float_set = {3.14, 1.0, 2.71, 0.5, 5.6}
    sorted_float_set = sort(float_set)
    print("Original set:", float_set)
    print("Sorted list from set:", sorted_float_set)

    non_iterable = {'a': 1, 'b': 2}  # Non-iterable input
    result = sort(non_iterable)
    print("Result:", result)