import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    # Sidenote: make sure you always refer to 'path' inside this
    # function, and not to a specific path string directly. Your
    # implementation may be called with different paths.
    if not os.path.exists(path):
        return None
    
    average = 0
    total_marks = 0
    # If the file is empty
    if os.stat(path).st_size == 0:
        return float(average)
    
    with open(path, 'r') as original_file:
        lines = original_file.readlines()
        total_lines = len(lines)
        n = 0
        for index, line in enumerate(lines):
            line = line.strip() 

            # ignore comment lines
            if "#" in line:
                continue
            # ignore empty lines
            elif not line:
                continue
            else:
                assert ':' in line
                subject, marks = line.split(':')
                n += 1
                total_marks += float(marks)

    average = round(total_marks / n, 2)
    average = float(average)
    return average


# The following line calls the function and prints the return
# value to the console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("assignment_10/my_grades.txt"))

