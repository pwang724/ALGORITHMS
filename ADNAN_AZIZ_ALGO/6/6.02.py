
def add_array(l):
    idx = len(l) - 1
    carry = 0

    while (idx >= 0):
        num = l[idx]

        if num == 9:
            l[idx] = 0
            carry = 1
            idx -= 1
        else:
            l[idx] += 1
            carry = 0
            break

    if carry & (idx < 0):
        l = [1] + l

    return l

l = [9, 9, 9]

print(add_array(l))