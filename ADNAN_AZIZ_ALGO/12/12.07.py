def min_max(l):
    comparator = l[0]
    cur_min_diff = 0
    cur_max_diff = 0
    cur_max = l[0]
    cur_min = l[0]

    for i in range(1, len(l)):
        diff = l[i] - comparator
        if diff > 0 and diff > cur_max_diff:
            cur_max_diff = diff
            cur_max = l[i]

        if diff < 0 and diff < cur_min_diff:
            cur_min_diff = diff
            cur_min = l[i]
    return cur_min, cur_max

def min_max_best(l):
    i = 0
    min_ = l[0]
    max_ = l[0]
    while (i +1) < l:
        if l[i] > l[i+1]:
            if l[i] > max_:
                max_ = l[i]
            if l[i+1] < min_:
                min_ = l[i+1]
        else: #i+1 is winner
            if l[i+1] > max_:
                max_ = l[i+1]
            if l[i] < min_:
                min_ = l[i]
        i += 2
    return (min_, max_)


if __name__ == '__main__':
    l = [3,2,5,1,2,4]
    print(min_max(l))
