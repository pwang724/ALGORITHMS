import numpy as np
import math as math

# long division
def divide_ld(x,y):
    result = 0
    while (x >= y):
        l = x
        power = 0
        while ((l >> 1) >= y):
                l = l >> 1
                power += 1
        l -= y
        x = l << power | (x & (1 << power) - 1)
        result = result | (1 << power)
    return result, x

# bitwise division
def divide(x,y):
    result = 0
    temp = x

    while (temp >= y):
        power = 0
        while (temp >= (y << power + 1)):
            power += 1
        temp -= y << power
        result = result | 1 << power
    return result, temp

# faster bitwise
def divide_faster(x,y):
    result = 0
    power = 32
    y_power = y << power
    while (x >= y):
        while (x < y_power):
            y_power = y_power >> 1
            power -= 1
        x -= y_power
        result += 1 << power
    return result



print(divide_ld(1000, 7))
print(divide_ld(230, 3))
print(divide_ld(11, 4))
