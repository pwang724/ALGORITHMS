def next_permutation(l):
    current_idx = len(l)-2
    while current_idx >= 0:
        if l[current_idx] > l[current_idx + 1]:
            current_idx -= 1
        else:
            break

    if current_idx >= 0:
        swap_idx = current_idx+1
        while ((swap_idx + 1) < len(l)):
            if l[swap_idx+1] < l[current_idx]:
                break
            else:
                swap_idx += 1

        l[current_idx], l[swap_idx] = l[swap_idx], l[current_idx]
        out = l[0:current_idx+1] + sorted(l[current_idx+1:])

    else:
        out = 'wtf'
    return out

if __name__ == "__main__":
    ordering = [3, 1, 2, 0]
    out = next_permutation(ordering)
    print(out)





