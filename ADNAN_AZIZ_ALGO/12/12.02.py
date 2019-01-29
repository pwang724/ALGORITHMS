def return_index(l):
    s = 0
    e = len(l)-1
    while (e > s):
        # m = (e+s)//2
        m = s + (e-s)//2
        if m == l[m]:
            return m
        elif l[m] > m:
            e = m -1
        else:
            s = m + 1
    return -1

if __name__ == '__main__':
    l = [-2, 0, 2,3,5,6, 7, 8, 9, 10, 11, 12]
    print(return_index(l))