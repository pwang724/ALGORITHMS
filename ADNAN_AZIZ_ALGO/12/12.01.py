import bisect

def find_first(l, val):
    i = bisect.bisect_left(l, val)
    return i

def binary_search(l, val):
    s = 0
    e = len(l)
    while (e >= s):
        m = (s+e)//2
        if l[m] == val:
            return m
        elif l[m] < val:
            s = m+1
        else:
            e = m-1
    return -1

def binary_match(l, val, s, e):
    while (e > s):
        m = (s+e)//2
        if l[m] == val:
            e = m
        else:
            s = m+1
    return s


#naive: rewind takes log(n), which is not good
def find_first_naive(l, val):
    a = binary_search(l, val)
    if a != -1:
        while l[a] == val:
            if a -1 >= 0 and l[a-1] == val:
                a -= 1
            else:
                return a
    else:
        return 'not found'

def find_first_better(l, val):
    e = binary_search(l, val)
    if e != -1:
        i = binary_match(l, val, 0, e)
        return i
    else:
        return 'not found'

def find_first_best(l, val):
    s = 0
    e = len(l)
    result = -1
    while (e >= s):
        m = (s+e)//2
        if l[m] == val:
            result = m
            e = m-1
        elif l[m] < val:
            s = m+1
        else:
            e = m-1
    return result


if __name__ == '__main__':
    l = [2,3,5,5,5,6,7]
    print(bisect.bisect_left(l, 5))
    print(find_first_better(l, 5))
    print(find_first_best(l, 5))

    # l = [5,5]
    # binary_match(l, 5, 0, 1)