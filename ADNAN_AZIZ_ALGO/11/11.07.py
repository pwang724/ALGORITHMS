import heapq

class stack:
    def __init__(self, k):
        self.__n = 0
        self.min_heap = []

        for i in k:
            heapq.heappush(self.min_heap, (self.__n, i))
            self.__n -= 1
        return

    def push(self, val):
        heapq.heappush(self.min_heap, (self.__n, val))
        self.__n -= 1

    def pop(self):
        tuple = heapq.heappop(self.min_heap)
        return tuple[1]

    def size(self):
        return len(self.min_heap)

class comparison:
    def __init__(self, function, elements = None):
        self.f = function
        if elements:
            self.heap = [(self.f(x), x) for x in elements]
            heapq.heapify(self.heap)
        else:
            self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, (self.f(val), val))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def size(self):
        return len(self.heap)

class stack1(comparison):
    def __init__(self, elements):
        self.__n = 0
        def f(x):
            a = self.__n
            self.__n -= 1
            return a
        super().__init__(lambda x: f(x), elements)



if __name__ == '__main__':
    a = stack1(['a','b','c','d'])
    a.push('e')

    while (a.size()):
        wtf = a.pop()
        print(wtf)


