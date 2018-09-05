def roman_conversation(str):
    dict = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}

    exception = 0
    result = dict[str[0]]

    i = 1
    while i < len(str):
        result += dict[str[i]]
        if ((str[i] == 'V' or str[i] == 'X') and str[i-1] == 'I') or \
            ((str[i] == 'L' or str[i] == 'C') and str[i - 1] == 'X') or \
            ((str[i] == 'D' or str[i] == 'M') and str[i - 1] == 'C'):
            result -= 2 * dict[str[i-1]]
            exception += 1
            if exception > 1:
                print('wtf')
        else:
            exception = 0
        i+= 1
    return result

if __name__ == '__main__':
    # print(roman_conversation('XXXXXIIIIIIIII'))
    # print(roman_conversation('LIX'))
    # print(roman_conversation('LVIIII'))
    print(roman_conversation('IXC'))



