class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = 0
        self._tail = 0
        self._num_queue_elements = 0
        return

    def enqueue(self, x):
        if len(self._entries) == self._num_queue_elements:
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head = 0
            self._tail = len(self._entries)
            self._entries += [None] * len(self._entries) * (Queue.SCALE_FACTOR - 1)

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1
        return

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('no more elements')
        self._num_queue_elements -= 1
        element = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return element

    def size(self):
        return self._num_queue_elements