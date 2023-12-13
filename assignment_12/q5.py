import random

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_length_global = 0
max_length_global = 5
char_start_global = 30
char_end_global = 65


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fuzzer(min_length, max_length, char_start, char_end):
    length = random.randint(min_length, max_length)
    result = ''
    for _ in range(length):
        result += chr(random.randint(char_start, char_end))
    return result


# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def calculate_factorial(inp):
    if inp is None:
        return None
    try:
        num = int(inp)
    except ValueError:
        raise TypeError("TypeError: string")
    if num < 0:
        raise ValueError("ValueError: number negative")
    elif num > 10:
        raise ValueError("ValueError: number too large")
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def run(trials):
    results = []
    
    for _ in range(trials):
        random_input = fuzzer(1, 5, 40, 60)  # Using global variables for fuzzer parameters
        try:
            factorial_result = calculate_factorial('random_input')
            results.append((0, "")) 
        except ValueError as e:
                results.append((1, str(e)))
        except:
            results.append((1, "Other error"))  # Other error tuple
    
    return results if results else []

# The following line calls the function run and prints the return
# value to the Console.
# print(fuzzer(5, 10, 43, 57))
print(run(1))