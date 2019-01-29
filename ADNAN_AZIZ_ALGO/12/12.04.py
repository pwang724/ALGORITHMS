def sqrt_floor(n):
    s = 0
    e = n
    while (s <= e):
        m = s + (e-s)//2
        if m**2 <= n and (m+1) **2 > n:
            return m
        elif m**2 < n:
            s = m+1
        else:
            e = m-1

if __name__ == '__main__':
    for i in range(27):
        print((sqrt_floor(i),i))

