import math

def palindrome(y):
    MSB = 0
    LSB = 0
    temp = y
    result = True
    while (temp // 10 > 0):
        temp /= 10
        MSB += 1

    while(y > 0 & result):
        a = y// (math.pow(10, MSB))
        b = y % (math.pow(10, LSB + 1))
        if a != b:
            result = False

        y = (y - a * math.pow(10, MSB)) // 10
        MSB -= 2

    return result

print(palindrome(121))
print(palindrome(1234))
print(palindrome(1221))
print(palindrome(987656789))