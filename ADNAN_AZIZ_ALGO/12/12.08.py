import heapq
import random

def k_largest(l, k):
    length = len(l)
    if k > length/2:
        k = length-k+1
        l = [x * -1 for x in l]
        f = lambda x: x * -1
    else:
        f = lambda x: x

    min_heap = l[:k]
    heapq.heapify(min_heap)

    for element in l[k:]:
        if element > min_heap[0]:
            heapq.heappushpop(min_heap, element)

    return f(min_heap[0])

def k_largest_best(l,k):
    def partition(s, e, pivot_idx):
        pivot_value = l[pivot_idx]
        new_pivot_idx = s
        l[pivot_idx], l[e] = l[e], l[pivot_idx]
        for i in range(s,e):
            if l[i] > pivot_value:
                l[i], l[new_pivot_idx] = l[new_pivot_idx], l[i]
                new_pivot_idx += 1
        l[e], l[new_pivot_idx] = l[new_pivot_idx], l[e]
        return new_pivot_idx

    s = 0
    e = len(l)-1
    while (True):
        idx_less = s
        pivot_index = random.randint(s,e)
        pivot_val = l[pivot_index]
        idx_less = partition(s,e, pivot_index)
        if idx_less == (k-1):
            return pivot_val
        elif idx_less > (k-1):
            e = idx_less - 1
        else: #number of elements is less than k
            s = idx_less + 1




if __name__ == '__main__':
    l = [3,2,5,1,6,4,10,9]
    for i in range(10):
        print(k_largest_best(l,1))