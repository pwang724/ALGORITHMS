import heapq
import functools

def compute_closest_stars(lol, k):
    def distance(coor):
        sq = map(lambda x: x**2, coor)
        return -1 * functools.reduce(lambda x, y: x+y, sq)

    min_heap = []
    star_iter = map(lambda x: (distance(x), x), lol)

    for i in range(k):
        star = next(star_iter, None)
        if star is not None:
            heapq.heappush(min_heap, star)

    star = next(star_iter, None)
    while star:
        if star[0] > min_heap[0][0]:
            heapq.heappushpop(min_heap, star)
        star = next(star_iter, None)

    result = []
    while min_heap:
        neg_distance, value = min_heap.pop()
        result.append(value)
    return result


if __name__ == '__main__':
    #assume sorted in increasing order
    a = [(1,0,0),(1,2,3),(2,3,4),(3,4,5),(1,1,1),(2,2,2)]
    print(compute_closest_stars(a, 3))