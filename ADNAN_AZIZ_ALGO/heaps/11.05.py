import heapq

def median_online(l):
    list_iter = iter(l)
    min_heap = []
    max_heap = []
    result = []
    max_over_min = 0

    n = next(list_iter)
    result.append(n)
    max_heap.append(-n)
    max_over_min += 1

    cur = next(list_iter, None)
    while (cur is not None):
        if cur >= result[-1]:
            heapq.heappush(min_heap, cur)
            max_over_min -= 1
        else:
            heapq.heappush(max_heap, -cur)
            max_over_min += 1

        if abs(max_over_min) == 2:
            if max_over_min > 0:
                temp = - heapq.heappop(max_heap)
                heapq.heappush(min_heap,temp)
            else:
                temp = heapq.heappop(min_heap)
                heapq.heappush(max_heap, - temp)
            max_over_min = 0

        #odd trials
        if max_over_min % 2:
            if max_over_min == 1:
                result.append(-1.0 * max_heap[0])
            else:
                result.append(1.0 * min_heap[0])
        #even trials
        else:
            mean = (min_heap[0] - max_heap[0]) / 2.0
            result.append(mean)
        cur = next(list_iter, None)
    return result

def median_online_better(sequence):
    sequence = iter(sequence)
    min_heap = []
    max_heap = []
    result = []

    #have to have first element
    a = next(sequence)
    min_heap.append(a)
    result.append(a)
    for x in sequence:
        if x >= result[-1]:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap,-x)

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, - heapq.heappop(max_heap))
        elif len(min_heap) > (len(max_heap) + 1):
            heapq.heappush(max_heap, - heapq.heappop(min_heap))

        if len(max_heap) == len(min_heap):
            result.append((min_heap[0] - max_heap[0]) / 2.0)
        else:
            result.append(1.0 * min_heap[0])
    return result

if __name__ == '__main__':
    print(median_online_better([1, 0, 3, 5, 2, 0, 1]))

    # 1, .5, 1, 2, 2, 1.5, 1