from binarytree import tree, bst, heap
import heapq
import itertools
from binarytree import Node

def top_k(k, stream):
# Entries are compared by their lengths.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        print(ord(next_string), ord(min_heap[0][1]))
        heap_print(list(map(lambda x: ord(x[1]), min_heap)))
        if min_heap[0][1] < next_string:
            heapq.heappushpop(min_heap, (len(next_string), next_string))
            heap_print(list(map(lambda x: ord(x[1]), min_heap)))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]

def heap_print(l):
    size = len(l)
    def helper(i):
        if i > (size - 1):
            return None
        else:
            a = Node(l[i], helper(2 * i + 1), helper(2 * i + 2))
        return a
    root = helper(0)
    print(root)

if __name__ is "__main__":
    stream = "The API below differs from textbook heap algorithms in two aspects: " \
          "(a) We use zero-based indexing. This makes the relationship between the " \
          "index for a node and the indexes for its children slightly less obvious, " \
          "but is more suitable since Python uses zero-based indexing. (b) " \
          "Our pop method returns the smallest item, not the largest " \
          "(called a “min heap” in textbooks; a “max heap” is more common in texts " \
          "because of its suitability for in-place sorting)."

    top_k(10, stream)