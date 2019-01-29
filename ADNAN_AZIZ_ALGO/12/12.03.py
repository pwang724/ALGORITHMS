def find_shift(l):
    assert(len(l) > 1)
    s = 0
    e = len(l) - 1
    while (s<e and l[e] < l[s]):
        m = s + (e-s) // 2
        if l[m] > l[m+1]:
            return m + 1
        elif l[m] > l[s]:
            assert(l[m] > l[e])
            s = m
        else:
            assert(l[m] < l[s])
            assert(l[m] < l[e])
            e = m
    return 0

def find_val(l, val):
    shift = find_shift(l)
    size = len(l)
    s = shift
    e = shift - 1
    f = lambda x: (x - shift + size) % size
    f_inv = lambda x: (x + shift) % size
    while (f(s) <= f(e)):
        f_m = f(s) + (f(e) - f(s))//2
        m = f_inv(f_m)
        if l[m] == val:
            return m
        elif l[m] < val:
            if f_m + 1 == size:
                return -1
            s = f_inv(f_m + 1)
        else:
            if f_m - 1 < 0:
                return -1
            e = f_inv(f_m - 1)
    return -1




if __name__ == '__main__':
    l = [1, 0]
    print(find_val(l, -1))