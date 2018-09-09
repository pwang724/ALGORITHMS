class Node:
    data = []
    nextNode = []

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:
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

    def cycle(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        a.nextNode = b
        b.nextNode = c
        c.nextNode = d
        d.nextNode = b

    def push(self, data):
        a = Node(data)
        a.nextNode = self.head
        self.head = a

    def pop(self):
        temp = self.head
        self.head = self.head.nextNode
        return temp

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while (cur.nextNode):
                cur = cur.nextNode
            cur.nextNode = Node(data)

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

    def reverse(self):
        prev = None
        cur = self.head

        while (cur != None):
            next = cur.nextNode
            cur.nextNode = prev
            prev = cur
            cur = next
        self.head = prev



if __name__ == '__main__':
    a = LinkedList()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('d')
    print(a.push('z'))
    print(a.pop())
    print(repr(a))
    a.reverse()
    print(repr(a))










