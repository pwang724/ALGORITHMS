def rle_encode(s):
    repeat = s[0]
    n = 1
    out = ''
    for i in range(1, len(s)):
        if s[i] == repeat:
            n+=1
        else:
            out += str(n) + repeat
            n=1
            repeat = s[i]
    out += str(n) + repeat
    return out

def rle_decode(s):
    repeat = s[::2]
    char = s[1::2]

    out = ''
    for r, c in zip(repeat, char):
        out += int(r) * c
    return out

def rle_decode1(s):
    i = 0
    n = 0
    out = ''
    while (i < len(s)):
        if s[i].isdigit():
            n += n * 10 + int(s[i])
        else:
            out += int(n) * s[i]
            n=0
        i+=1
    return out


if __name__ == '__main__':
    print(rle_encode('abbccc'))
    print(rle_decode1('1a2b3c'))