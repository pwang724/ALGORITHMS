class Queue:
    def __init__(self):
        self._data = []

    #inject
    def enqueue(self, x):
        self._data.append(x)

    #pop, popleft
    def dequeue(self):
        return self._data.pop(0)

    def size(self):
        return len(self._data)

    def max(self):
        return max(self._data)

    def peek(self):
        return self._data[0]

    #eject
    def eject(self):
        return self._data.pop()

    #push
    def push(self, n):
        return self._data.insert(n, 0)

