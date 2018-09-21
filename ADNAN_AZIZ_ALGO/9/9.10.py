class Queue:
    def __init__(self):
        self._data = []
        self._max = [] #max is a stack

    def dequeue(self):
        a = self._data[0]
        if a == self.max():
            self._max.pop(0)
        return self._data.pop(0)

    def enqueue(self, x):
        self._data.append(x)
        while(len(self._max) and x > self._max[-1]):
            self._max.pop()
        self._max.append(x)

    def max(self):
        return self._max[0]

if __name__ == '__main__':
    a = Queue()
    a.enqueue(1)
    a.enqueue(5)
    a.enqueue(5)
    a.enqueue(3)
    a.enqueue(7)
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(9)
