import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    
    # Create the output file if it doesn't exist
    if not os.path.exists(path_writing):
        open(path_writing, 'w').close()
    
    # If the file is empty
    if os.stat(path_reading).st_size == 0:
        with open(path_writing, 'w') as processed_file:
            processed_file.write('')
            return True
    
    with open(path_reading, 'r') as original_file:
        with open(path_writing, 'w') as processed_file:
            lines = original_file.readlines()
            total_lines = len(lines)
            found_name = False
            for index, line in enumerate(lines):
                line = line.strip() 
                if line == "Name":
                    processed_file.write('Firstname,Lastname\n')
                    found_name = True
                elif found_name == False and not line:
                    continue
                else:
                    if not line:  # Empty line
                        processed_file.write(',\n')
                    else:
                        firstname, lastname = '', ''
                        if ';' in line:  
                            lastname, firstname = line.split(';')
                        elif ' ' in line:
                            firstname, lastname = line.split(' ')
                        firstname = firstname.strip()
                        lastname = lastname.strip()
                        if index == total_lines - 1:  # Last line
                            processed_file.write(f'{firstname},{lastname}')  # No newline for last line
                        else:
                            processed_file.write(f'{firstname},{lastname}\n')

    return True

if __name__ == "__main__":
    INPUT_PATH = "assignment_10/my_data.txt"
    OUTPUT_PATH = "assignment_10/my_data_processed.txt"
    process_data(INPUT_PATH, OUTPUT_PATH)
    if os.path.exists(OUTPUT_PATH):
        with open(OUTPUT_PATH) as resultfile:
            print(resultfile.read())
    else:
        print("No output file exists")
    