def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = (L + U) // 2
        if A[M] < t:
            L=M+1
        elif A[M] == t:
            return M
        else:
            U=M-1
    return -1

if __name__ == "__main__":
    bsearch(6,[5,6])