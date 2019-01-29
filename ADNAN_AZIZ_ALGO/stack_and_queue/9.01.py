class Stack:
    head = None
    tail = None
    data = []
    max_list = []
    max_val = 0

    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(list(reversed(self.data)))

    def size(self):
        return len(self.data)

    def push(self, d):
        prev_max = self.max_val
        self.max_val = max(prev_max, d)
        self.max_list.append(prev_max)
        self.data.append(d)

    def pop(self):
        if len(self.data):
            val = self.data.pop()
            max = self.max_list.pop()
            return val
        else:
            return 'empty list'

    def peek(self):
        if len(self.data):
            return self.data[-1]
        else:
            return 'empty list'

    def max(self):
        if len(self.max_list):
            return self.max_list[-1]
        else:
            return 'empty list'




if __name__ == '__main__':
    a = Stack()
    a.push(0)
    a.push(2)
    a.push(4)
    a.push(1)
    a.push(3)
    # print(a)
    print(a.peek())
    a.push(5)
    print(a)
    a.pop()
    print(a)











