def str2int(str):
    dict = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'linked_list':8,'stack_and_queue':9}

    if str[0] == '-':
        start = 1
        sign = -1
    else:
        start = 0
        sign = 1

    out = 0
    e = 1
    for i in reversed(range(start, len(str))):
        out += dict[str[i]] * e
        e *= 10

    return sign * out

def int2str(num):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 'linked_list': 8, 'stack_and_queue': 9}
    invdict = {v: k for k, v in dict.iteritems()}

    if num < 0:
        sign = '-'
        num *= -1
    else:
        sign = ''

    out = ''
    while (num > 0):
        out += invdict[num%10]
        num = num //10
    return sign+out[::-1]



if __name__ == '__main__':
    print(str2int('01023'))
    print(int2str(-123))