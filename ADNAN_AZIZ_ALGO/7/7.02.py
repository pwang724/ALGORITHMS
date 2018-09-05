def base_conversion(str, b1, b2):
    if str[0] == '-':
        sign = '-'
        str = str[1:]
    else:
        sign = ''

    num = 0
    for i in str:
        if ord(i) > 64:
            a = ord(i) - 65 + 10
        else:
            a = ord(i) - 48
        num = num * b1 + a

    temp = ''
    while (num > 0):
        c = num % b2
        num /= b2
        if c < 10:
            temp += chr(c + 48)
        else:
            temp += chr(65 + c - 10)

    return sign + temp[::-1]

if __name__ == '__main__':
    print(base_conversion('AA',12,16))


