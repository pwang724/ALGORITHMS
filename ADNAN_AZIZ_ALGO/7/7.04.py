#silly problem, real solution has no additional space

def replace_and_delete(str, size):
    str = str[:size]
    key = []
    for i, alphabet in enumerate(str):
        if alphabet == 'a':
            key.append((i,'rep'))
        if alphabet == 'b':
            key.append((i,'del'))

    result = ''
    idx = 0
    for k in key:
        nextidx = k[0]
        operation = k[1]

        if operation == 'rep':
            result += str[idx:nextidx] + 'dd'
        if operation == 'del':
            result += str[idx:nextidx]
        idx = nextidx + 1
    result += str[idx:]

    return result

if __name__ == '__main__':
    str = 'acdbbca'
    str1 = 'abac'
    print(replace_and_delete(str,7))
    print(replace_and_delete(str1,4))

