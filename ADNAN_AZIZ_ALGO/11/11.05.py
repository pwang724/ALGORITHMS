import heapq

def median(l):
    l = iter(l)
    min_heap = []
    max_heap = []
    result = []

    a = next(l)
    result.append(a)
    max_heap.append(-a)
    max_over_min = 1

    cur = next(l, None)
    while (cur is not None):
        if cur >= result[-1]:
            heapq.heappush(min_heap, cur)
            max_over_min -= 1
        else:
            heapq.heappush(max_heap, -cur)
            max_over_min += 1

        if abs(max_over_min) == 2:
            if max_over_min > 0:
                val = - heapq.heappop(max_heap)
                heapq.heappush(min_heap, val)
            else:
                val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -val)
            max_over_min = 0

        if max_over_min % 2: #odd
            if max_over_min == 1:
                result.append(-1.0 * max_heap[0])
            else:
                result.append(1.0 * min_heap[0])
        else:
            result.append((-max_heap[0] + min_heap[0])/2.)


        cur = next(l, None)

    return result

if __name__ == '__main__':
    l = [1, 0, 3, 5, 2, 0, 1]
    r = [1, .5, 1, 2, 2, 1.5, 1]

    print(median(l))