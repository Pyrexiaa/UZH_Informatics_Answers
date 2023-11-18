import math

def zoo(number):
    # return a tuple containing the required values
    down_number = math.floor(number)
    up_number = math.ceil(number)
    arc_tangent = math.atan(number)
    fractional, integer = math.modf(number)
    my_tuple = (fractional, integer)
    next_after = math.nextafter(number, -math.inf)
    cube_root = math.cbrt(number)
    return (down_number, up_number, arc_tangent, my_tuple, next_after, cube_root)

result = zoo(26.11)
print(result)