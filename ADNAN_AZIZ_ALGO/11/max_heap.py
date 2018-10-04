#good for fast inserts log n as compared to sorted stack insertions (n). deletions / pops are also log n, which is longer
#compared to sorted stack (1). if there are many insertions and few pops, use heap
from binarytree import Node

class max_heap:
    l = []

    def __init__(self):
        self.l = []

    def size(self):
        return len(self.l)

    def heapify(self, l):
        self.l = l
        last_element = len(l) // 2
        for i in reversed(range(last_element)):
            self.__siftdown(i)

    def push(self, element):
        self.l.append(element)
        self.__siftup(self.size()-1)

    def pop(self, i):
        if not self.size():
            return 'empty list'
        element = self.peek()

        len = self.size()
        self.__swap(i, len - 1)
        self.l.pop()

        self.__siftdown(i)
        return element

    def pushpop(self,k):
        self.push(k)
        return self.pop(0)

    def peek(self):
        if self.l:
            return self.l[0]

    def __siftup(self, idx):
        parent_index = self.__parent(idx)
        if parent_index is None:
            return

        if self.l[parent_index] < self.l[idx]:
            self.__swap(idx, parent_index)
            self.__siftup(parent_index)

    def __siftdown(self, idx):
        lc_index = self.__leftchild(idx)
        rc_index = self.__rightchild(idx)

        if not lc_index and not rc_index:
            return
        elif lc_index and not rc_index:
            max_index = lc_index
        else:
            max_index = lc_index if self.l[lc_index] >= self.l[rc_index] else rc_index

        if self.l[max_index] > self.l[idx]:
            self.__swap(max_index, idx)
            self.__siftdown(max_index)


    def __swap(self, i, j):
        self.l[i], self.l[j] = self.l[j], self.l[i]

    def __parent(self, i):
        if i == 0:
            return None
        else:
            return int((i-1)/2)

    def __leftchild(self, i):
        idx = (2*i) + 1
        if idx < self.size():
            return idx
        else:
            return None

    def __rightchild(self, i):
        idx = (2*i) + 2
        if idx < self.size():
            return idx
        else:
            return None

    def print(self):
        l = self.l
        size = self.size()

        def helper(i):
            if i > (size-1):
                return None
            else:
                a = Node(l[i], helper(2*i +1), helper(2*i + 2))
            return a
        root = helper(0)
        print(root)

if __name__ == '__main__':
    l = [561, 314, 401, 28, 156, 359, 271, 11, 3, 100]
    l1 = list(l)
    l1.sort()
    print(l1)
    heap = max_heap()
    heap.heapify(l1)
    heap.print()

    heap.l = l
    heap.print()

    # heap.push(500)
    # heap.print()
    # heap.pop(2)
    # heap.print()
    # print(heap.pushpop(2))
    # heap.print()

