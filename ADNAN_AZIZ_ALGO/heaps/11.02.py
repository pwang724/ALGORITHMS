# from heaps.01 import merge_lists_better
import heapq

def sort_inc_dec(l, idx):
    lol = []
    inc = 1
    for i in range(len(idx)-1):
        if inc:
            temp = iter(l[idx[i]:idx[i + 1]])
            # print(list(temp))
            lol.append(temp)
        else:
            temp = reversed(l[idx[i]:idx[i + 1]])
            # print(list(temp))
            lol.append(temp)
        inc^=1
    return merge_lists_better(lol)

def merge_lists_better(lol):
    min_heap = []
    result = []
    #put first element
    for cl, l in enumerate(lol):
        val = next(l, None)
        if val is not None:
            heapq.heappush(min_heap, (val, cl))

    while (min_heap):
        val, cl = heapq.heappop(min_heap)
        result.append(val)
        nextElement = next(lol[cl], None)
        if nextElement is not None:
            heapq.heappush(min_heap, (nextElement, cl))
    return result

if __name__ == '__main__':
    #assume sorted in increasing order
    a = [0,3,9,12,10,8,6,11,15,2,1]
    idx = [0,3,6,8,len(a)-1]

    print(sort_inc_dec(a, idx))