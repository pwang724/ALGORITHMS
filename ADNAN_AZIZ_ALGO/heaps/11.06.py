import heapq

def sort_k_largest(l, k):
    length = len(l)
    result = []
    indices = [0]
    for _ in range(k):
        max_idx = indices[0]
        indices_idx = 0
        for i, idx in enumerate(indices):
            if l[idx] > l[max_idx]:
                max_idx = idx
                indices_idx = i

        result.append(l[max_idx])
        indices.pop(indices_idx)
        if 2*max_idx+1 < length:
            indices.append(2*max_idx + 1)
        if 2*max_idx+2 < length:
            indices.append(2*max_idx + 2)
    return result

def sort_k_largest_better(l,k):
    l = list(map(lambda x: x * -1, l))
    size = len(l)
    result = []
    max_heap = [(l[0], 0)]

    for _ in range(k):
        max, idx = heapq.heappop(max_heap)
        result.append(-max)

        left= 2*idx+1
        right = 2*idx+2
        if left < size:
            heapq.heappush(max_heap, (l[left], left))
        if right < size:
            heapq.heappush(max_heap, (l[right], right))
    return result







if __name__ == '__main__':
    l = [561, 314, 401, 28, 156, 359, 271, 11, 3, 100]
    l = [10, 8, 9, 7.5, 6, 7, 5, 6, 6.5]
    print(sort_k_largest_better(l, 5))