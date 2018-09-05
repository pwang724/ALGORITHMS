def reverse_sentence(str):
    i = len(str)
    j = len(str)-1

    result = ''
    while (i>=0 and j>=0):
        if str[j]== ' ':
            result+= str[j+1:i] + ' '
            i = j
        j-= 1
    return result + str[0:i]

def reverse_in_place(str):
    #silly get around for the fact that strings are immutable in python
    def swap(c, i, j):
        cl = list(c)
        cl[i], cl[j] = cl[j], cl[i]
        return ''.join(cl)

    str = str[::-1]
    s = 0
    j = 0
    while len(str) > j:
        if j == len(str)-1:
            word_len = 1 + j - s
            for i in range((word_len / 2)):
                str = swap(str, s+i, s + word_len - i - 1)
            j+= 1

        elif str[j] == ' ':
            word_len = j - s
            for i in range((word_len / 2)):
                str = swap(str, s+i, s + word_len - i - 1)
            s = j+1
            j = s
        else:
            j+=1
    return str




if __name__ == '__main__':
    print(reverse_in_place('adfad fdas like alice'))
