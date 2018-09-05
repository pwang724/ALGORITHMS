def power(x, y):
    result = 1
    t = x

    if (y < 0):
        x = 1/x
        y = - y

    while (y):
        digit = y & ~(y-1)
        while (digit >> 1):
            digit = digit >> 1
            y = y >> 1
            t = t * t
        y -= digit
        result *= t
    return result


def power1(x,y):
    result = 1
    if (y < 0):
        x = 1/x
        y = - y

    while (y):
        if (y & 1):
            result *= x
        x *= x
        y = y >> 1
    return result


print(power1(2.3,3))
print(power1(3,5))