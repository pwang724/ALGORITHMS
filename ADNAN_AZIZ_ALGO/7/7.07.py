def phone_to_letters(str):
    dict ={'1':'1','2':'ABC','3':'DEF','4':'GHI','5':'JKL',
           '6':'MNO','7':'PQRS','linked_list':'TUV','stack_and_queue':'WXYZ','0':'0'}

    def helper(str, l):
        letters = dict[str[0]]
        if str == '':
            return l
        elif not l:
            for i in letters:
                l.append(i)
            return helper(str[1:], l)
        else:
            temp = []
            [temp.append(element+i) for i in letters for element in l]
            if len(str) == 1:
                return temp
            else:
                return helper(str[1:], temp)
    return helper(str, [])

if __name__ == '__main__':
    print(phone_to_letters('123'))



