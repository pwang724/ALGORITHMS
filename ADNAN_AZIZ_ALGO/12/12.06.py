import bisect

def search_2D(mat, val):
    n_r = len(mat)
    n_c = len(mat[0])
    start = 0
    row_end = n_r
    col_end = n_c

    row_f = lambda i: [x[i] for x in mat]
    while (start <= row_end or start <= col_end):
        col_mid = bisect.bisect_left(mat[start][start:col_end], val) + start
        row_vec = row_f(start)
        row_mid = bisect.bisect_left(row_vec[start:row_end], val) + start
        if col_mid < n_c:
            if mat[start][col_mid] == val:
                return (start, col_mid)
            else:
                col_end = col_mid

        if row_mid < n_r:
            if mat[row_mid][start] == val:
                return (row_mid, start)
            else:
                row_end = row_mid
        start += 1
    return -1

def search_2D_better(mat, val):
    n_r = len(mat)
    n_c = len(mat[0])
    cur_r = 0
    col_end = n_c
    while (cur_r < n_r):
        cur_c = bisect.bisect_left(mat[cur_r][:col_end], val)
        if cur_c < n_c:
            col_end = cur_c
            if mat[cur_r][cur_c]== val:
                return (cur_r, cur_c)
        cur_r += 1
    return -1

def search_2D_best(mat, val):
    n_r = len(mat)
    n_c = len(mat[0])
    cur_r = 0
    cur_c = n_c-1
    while (cur_c >= 0 and cur_r < n_r):
        if mat[cur_r][cur_c] == val:
            return (cur_r, cur_c)
        elif mat[cur_r][cur_c] < val:
            cur_r += 1
        else:
            cur_c -= 1


if __name__ == '__main__':
    mat = [[-1,2,4,4,6],
           [1,5,5,9,21],
           [3,6,6,9,22],
           [3,6,8,10,24],
           [6,8,9,12,25],
           [8,10,12,13,40]]
    print(search_2D_best(mat, 14))


