class Node:
    data = []
    nextNode = []

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    head = None
    tail = None

    def __init__(self):
        self.head = None

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

    def reverse(self, data):
        prev = None
        cur = self.head
        next = None

        while (cur.nextNode != None):
            if prev != None:
                cur.nextNode = prev
            pre = cur
            cur = next


if __name__ == '__main__':
    a = LinkedList()










