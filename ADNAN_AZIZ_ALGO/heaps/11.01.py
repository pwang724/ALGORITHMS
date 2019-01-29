import heapq
import itertools
from binarytree import Node

def merge_lists(lol):
    lol_iters = []
    result = []
    lol_len = list(map(lambda x: len(x), lol))
    for i, l in enumerate(lol):
        lol_iters.append(list(map(lambda x: (x, i), l)))

    #take first elements of each
    min_heap = list(map(lambda x: x[0], lol_iters))
    heapq.heapify(min_heap)
    lol_idx = [1] * len(lol)

    while (min_heap):
        element = heapq.heappop(min_heap)
        val, cl = element[0], element[1]
        result.append(val)
        if lol_idx[cl] < lol_len[cl]:
            heapq.heappush(min_heap, lol_iters[cl][lol_idx[cl]])
            lol_idx[cl]+=1
    return result

def merge_lists_better(lol):
    lol_iters = [iter(x) for x in lol]
    min_heap = []
    result = []
    #put first element
    for cl, l in enumerate(lol_iters):
        val = next(l, None)
        if val is not None:
            heapq.heappush(min_heap, (val, cl))

    while (min_heap):
        val, cl = heapq.heappop(min_heap)
        result.append(val)
        nextElement = next(lol_iters[cl], None)
        if nextElement is not None:
            heapq.heappush(min_heap, (nextElement, cl))
    return result

def pythonic_merge(lol):
    return list(heapq.merge(*lol))


if __name__ == '__main__':
    a = [3,5,7]
    b = [0,6]
    c = [0,6,28]
    lol = [a,b,c]
    print(merge_lists_better(lol))