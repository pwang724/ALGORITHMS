def binary_search(l, val):
    s = 0
    e = len(l)-1
    while (e >= s):
        m = (e + s)//2
        if l[m] == val:
            return m
        elif l[m] < val:
            s = m + 1
        else:
            e = m - 1
    return -1

if __name__ == '__main__':
    l = [0, 1, 2]
    binary_search(l, 2)