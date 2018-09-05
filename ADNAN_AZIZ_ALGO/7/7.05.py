#dumb
def palindrome(str):
    i = 0
    j = len(str)-1
    ord_i = ord(str[i])
    ord_j = ord(str[j])

    while (j > i):
        while (
                not (ord_i >= 48 and ord_i <= 57) and
                not (ord_i >= 65 and ord_i <= 90) and
                not (ord_i >= 97 and ord_i <= 122)):
            i+= 1
            ord_i = ord(str[i])
        if (ord_i >= 65 and ord_i <= 90):
            ord_i += 32

        while (
                not (ord_j >= 48 and ord_j <= 57) and
                not (ord_j >= 65 and ord_j <= 90) and
                not (ord_j >= 97 and ord_j <= 122)):
            j -= 1
            ord_j = ord(str[j])
        if (ord_j >= 65 and ord_j <= 90):
            ord_j += 32

        if ord_i != ord_j:
            return False

        i += 1
        ord_i = ord(str[i])
        j -= 1
        ord_j = ord(str[j])
    return True

#smart
def palindrome1(str):
    i = 0
    j = len(str)-1

    while (j > i):
        while (not str[i].isalnum()):
            i+= 1
        while (not str[j].isalnum()):
            j-= 1
        if str[i].lower() != str[j].lower():
            return False
        i+=1
        j-=1
    return True

if __name__ == '__main__':
    print(palindrome1('A Man, a plan, a canal, Panama'))
    print(palindrome1('Able was I, ere I saw Elba!'))
    print(palindrome1('Ray a Ray'))


