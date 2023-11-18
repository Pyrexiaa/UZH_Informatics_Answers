def gcd(a, b):
    a, b = abs(a), abs(b)
    
    if a == 0 and b == 0:
        raise ValueError("Both numbers cannot be zero")

    if a == 0 or b == 0:
        return max(a, b)

    return gcd(b, a % b)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 12
b = 6
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")