def all_ip():
    ip = '19216811'
    n = len(ip) - 2

    def helper(n_periods, L):
        if n_periods == 0:
            return L
        else:
            temp = []
            [temp.append(l + [l[-1]+i]) for l in L for i in range(1,4) if l[-1]+i <= n]
            return helper(n_periods-1, temp)
    result = helper(2, [[0],[1],[2]])
    [r.append(n+1) for r in result]

    out = []
    for l in result:
        boo = True
        i = 1
        while (boo and (i < len(l))):
            if int(ip[1+l[i-1]:1+l[i]]) > 255:
                boo = False
            i+= 1
        if boo:
            newip = ip[:l[0]+1] + '.' + ip[l[0]+1:l[1]+1] + '.' + ip[l[1]+1:l[2]+1] + '.' + ip[l[2]+1:] + '.'
            out.append(newip)
    return out

if __name__ == '__main__':
    print(all_ip())