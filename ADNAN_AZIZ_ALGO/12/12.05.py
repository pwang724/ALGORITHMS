def sqrt_floor(s, e, n, increment):
    while (s <= e):
        m = s + (e-s)//2
        if m**2 <= n and (m+increment) **2 > n:
            return m
        elif m**2 < n:
            s = m+increment
        else:
            e = m-increment

def sqrt_main(n):
    tol = .1
    inc = 1.0
    s = 0
    e = n
    while (True):
        result = sqrt_floor(s, e, n, inc)
        if (n - result ** 2) < tol:
            return (result, inc)
        s = result
        e = result + inc
        inc /= 2.0

def sqrt_best(n):
    if n > 1.0:
        tol = .1
        s = 0
        e = float(n)
    else:
        tol = .01
        s = n
        e = 1.0

    while (True):
        m = s + (e-s) / 2
        if abs(m ** 2 - n) > tol and m ** 2 > n:
            e = m
        elif abs(m ** 2 - n) > tol and m ** 2 < n:
            s = m
        else:
            return m


if __name__ == '__main__':
    print(sqrt_best(.5))

