class Node:
    data = []
    nextNode = []

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return repr(self.data)


class Stack:
    head = None
    tail = None

    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        nodes = []
        j = 0
        while cur and j < 20:
            nodes.append(repr(cur))
            cur = cur.nextNode
            j+= 1
        return '[' + ', '.join(nodes) + ']'

    def size(self):
        s = 0
        cur = self.head
        while (cur):
            s+= 1
            cur = cur.nextNode
        return s

    def push(self, data):
        a = Node(data)
        a.nextNode = self.head
        self.head = a

    def pop(self):
        temp = self.head
        self.head = self.head.nextNode
        return temp

    def peek(self):
        return self.head


    def delete(self, k):
        if self.head.data == k:
            self.pop()
        else:
            prev = self.head
            cur = self.head.nextNode
            while (cur and cur.data != k):
                prev = cur
                cur = cur.nextNode
            prev.next = cur.nextNode

    def search(self, data):
        cur = self.head
        while cur != None and cur.data != data:
            cur = cur.nextNode
        return cur



if __name__ == '__main__':
    a = Stack()
    a.push(0)
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print(a)

    cur = a.head
    while(cur):
        print(cur)
        cur = cur.nextNode










