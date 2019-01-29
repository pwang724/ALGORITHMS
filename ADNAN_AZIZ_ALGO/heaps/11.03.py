import heapq

def almost_sorted(l, k):
    start = k
    min_heap = l[0:start]
    heapq.heapify(min_heap)
    result = []

    # how solution does it
    # for x in itertools.islice(sequence, k):
    #     heapq.heappush(min_heap, x)
    for i in range(start, len(l)):
        element = heapq.heappushpop(min_heap, l[i])
        result.append(element)

    #sequence is exhausted
    while (min_heap):
        result.append(heapq.heappop(min_heap))
    return result

if __name__ == '__main__':
    #assume sorted in increasing order
    a = [4, 2, 6, 1, 5, 3, 7]

    print(almost_sorted(a, 3))

