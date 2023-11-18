# build a string 
def build_string_pyramid(h):

    result = ""
    ranges = h*2-1
    minus_number = 2

    for i in range(ranges):
        s = ""
        if i <= ranges // 2:
            for j in range(i+1):
                if j == 0:
                    s = s + str(j+1)
                else:
                    s = s + "*" + str(j+1)
        else:
            new_range = i - minus_number
            for j in range(new_range+1):
                if j == 0:
                    s = s + str(j+1)
                else:
                    s = s + "*" + str(j+1)
            minus_number = minus_number+2
            
        result += s + "\n"
    return result

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid(5))