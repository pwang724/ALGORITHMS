def unique(l):
    comp = l[0]
    goodidx = 1
    for idx in range(1, len(l)):
        value = l[idx]
        if value == comp:
            print('nothing')
        else:
            comp = l[idx]
            if idx != goodidx:
                l[goodidx], l[idx] = l[idx], l[goodidx]
            goodidx += 1
    return l, goodidx

if __name__ == "__main__":
    l = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6]
    print(unique(l))
