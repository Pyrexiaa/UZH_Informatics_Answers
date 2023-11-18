
# You need to complete this function.
# The numbers must be valid according to description before determining friendly parity situations.
# Return the string "Invalid" if they are not valid.
def is_friendly_pair(num1, num2):
    if num1 > 0 and isinstance(num1, int) and num2 > 0 and isinstance(num2, int) and num1 != num2:
        num1_divisors = []
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                num1_divisors.append(i)
        num2_divisors = []
        for i in range(1, num2 + 1):
            if num2 % i == 0:
                num2_divisors.append(i)
        num1_abundancy = sum(num1_divisors) / num1
        num2_abundancy = sum(num2_divisors) / num2
        if num1_abundancy == num2_abundancy:
            return True
        else:
            return False
    else:
        return "Invalid"

#This line prints your method's return so that you can check your output.
print(is_friendly_pair(6, 28))
