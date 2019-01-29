from Stack_List import Stack

class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def dequeue(self):
        if not self.dequeue_stack.size():
            while (self.enqueue_stack.size()):
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()


    def enqueue(self, x):
        self.enqueue_stack.push(x)

if __name__ == '__main__':
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a.dequeue())
    a.enqueue(4)
    print(a.dequeue())

