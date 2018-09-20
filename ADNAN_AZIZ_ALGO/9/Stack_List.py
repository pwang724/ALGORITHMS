class Stack:
    head = None
    tail = None
    data = []

    def __init__(self):
        self.head = None
        self.data = []

    def __repr__(self):
        return repr(list(reversed(self.data)))

    def size(self):
        return len(self.data)

    def push(self, d):
        self.data.append(d)

    def pop(self):
        if len(self.data):
            return self.data.pop()
        else:
            return 'empty list'

    def peek(self):
        if len(self.data):
            return self.data[-1]
        else:
            return None



if __name__ == '__main__':
    a = Stack()
    a.push(0)
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    # print(a)
    print(a.peek())
    a.push(5)
    print(a)
    a.pop()
    print(a)











