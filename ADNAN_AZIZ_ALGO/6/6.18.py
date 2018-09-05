def rotate90(m):
    n = len(m)
    b = [[] for i in range(n)]
    for j in range(0,n):
        for i in reversed(range(0,n)):
            b[j].append(m[i][j])
    return b

def rotate90_inplace(m):
    s = 0
    e = len(m) - 1

    while e > s:
        for i in range(e-s):
            m[s][s+i], m[s+i][e], m[e][e-i], m[e-i][s] = \
                m[e-i][s], m[s][s+i], m[s+i][e], m[e][e-i]
        s += 1
        e -= 1

    return m


if __name__ == '__main__':
    n = 6
    a = [[j*n + i+1 for i in range(n)] for j in range(n)]
    print(rotate90_inplace(a))