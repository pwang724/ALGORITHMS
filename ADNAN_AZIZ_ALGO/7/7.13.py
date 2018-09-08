def search(s,t):
    l_s = len(s)
    l_t = len(t)
    i = 0
    while i < l_t:
        if (s[0] == t[i]) and (s[-1] == t[i + l_s -1]):
            if s == t[i:i+l_s + 1]:
                return i
            else:
                i += l_s
        else:
            i += l_s
    return 0

#TODO determine precise values of mod and factor
def rabin_karp(p,t):
    def get_hash(x, mod, factor):
        out = 0
        for c in x:
            out = (out * factor + ord(c)) % mod
        return out

    mod = 101
    factor = 256
    l = len(p)
    p_hash = get_hash(p, mod, factor)
    t_hash = get_hash(t[:3], mod, factor)
    const = (256 ** (l-1)) % mod

    for c in range(3, len(t)+1):
        if (p_hash == t_hash) and t[c-l:c] == p:
            return c - l
        else:
            old = (const * ord(t[c-l])) % mod
            new = ord(t[c])
            t_hash = ((t_hash + mod - old) * factor + new) % mod
    return 0

def kmp(p, t):
    def search(i,j):
        headidx = 0
        headchange = 0
        wrongidx_p, wrongidx_t = i, j
        for idxt, idxp in enumerate(range(i, len(p))):
            if t[j+idxt] == p[0] and headchange == 0 and idxt != 0:
                headchange += 1
                headidx = len(p) - idxt - 1

            if (idxp == len(p) -1) and p[idxp] == t[j+idxt]:
                return -1, -1
            elif p[idxp] != t[j+idxt]:
                wrongidx_p, wrongidx_t = idxp, j + idxt
                break
        return headidx, wrongidx_t

    i_p = 0
    j_t = 0
    while (j_t < len(t)):
        headidx, wrongidx_t = search(i_p,j_t)
        print(headidx, wrongidx_t)
        if headidx == -1:
            return j_t - i_p
        if (i_p == 0) and (wrongidx_t == j_t):
            j_t = wrongidx_t +1
        else:
            j_t = wrongidx_t
        i_p = headidx

    return 0



if __name__ == '__main__':
    # print(search('wtf','wafwbfwtf'))
    # print(rabin_karp('wtf','wafwbfwtf'))
    print(kmp('ABCDABD', 'ABC ABCDAB ABCDABCDABDE'))