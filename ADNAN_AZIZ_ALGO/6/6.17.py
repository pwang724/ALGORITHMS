def spiral(A):
    A_t = [list(i) for i in zip(*A)]

    i_start = 0
    i_end = len(A)-1

    result = []
    while (i_start < i_end):
        l_r = A[i_start][i_start:i_end+1]
        l_r.pop()
        t_d = A_t[i_end][i_start:i_end+1]
        t_d.pop()
        r_l = A[i_end][i_start:i_end+1]
        r_l.reverse()
        r_l.pop()

        d_t = A_t[i_start][i_start:i_end+1]
        d_t.reverse()
        d_t.pop()

        result += l_r + t_d + r_l + d_t
        i_start += 1
        i_end -= 1

    if i_start == i_end:
        result.append(A[i_start][i_start])

    return result

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[1,2],[3,4]]
    C = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(spiral(A))
    print(spiral(B))
    print(spiral(C))