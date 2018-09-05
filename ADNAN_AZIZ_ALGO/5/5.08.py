def reverse(x):
    temp = abs(x)
    result = 0
    while (temp):
        rem = temp % 10
        result = result * 10 + rem
        temp = temp // 10

    result = result if x > 0 else -result
    return result

print(reverse(123456))