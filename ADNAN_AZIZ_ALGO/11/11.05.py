import heapq

def median_online(l):
    list_iter = iter(l)
    min_heap = []
    max_heap = []
    result = []
    median = 0
    even = 1

    #init
    a = next(list_iter)
    b = next(list_iter)
    if a >=b:
        min_heap.append(a)
        max_heap.append(-b)
    else:
        min_heap.append(b)
        max_heap.append(-a)
    result.append(a)
    result.append((a+b)/2)

    while (True):
        num = next(list_iter, None)
        if num is None:
            return

        if num >= result[-1]:
            median = heapq.heappushpop(min_heap, num)
            heapq.heappush(max_heap, -median)
        else:
            median = -1 * heapq.heappushpop(max_heap, -num)
            heapq.heappush(min_heap, median)

        result.append(median)


    return

if __name__ == '__main__':
    #assume sorted in increasing order
    a = [(1,0,0),(1,2,3),(2,3,4),(3,4,5),(1,1,1),(2,2,2)]
    print(median_online([1, 0, 3, 5, 2, 0, 1]))

    # 1, .5, 1, 2, 2, 1.5, 1