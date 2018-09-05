def pascal(n):
    def makerow(l):
        out = [1]
        for i in range(1,len(l)):
            out.append(l[i] + l[i-1])
        out.append(1)
        return out

    tri = []
    tri.append([1])
    tri.append([1,1])
    for i in range(2,n):
        a = makerow(tri[i-1])
        tri.append(a)
    return tri


if __name__ == '__main__':
    print(pascal(10))