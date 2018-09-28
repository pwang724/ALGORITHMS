# A binary tree node
class Node:
    def __repr__(self):
        return repr(self.data)

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.done = None

def inOrder(root):
    cur = root
    s = []
    while (True):
        while cur:
            s.append(cur)
            cur = cur.left
        if len(s):
            a = s.pop()
            print(a.data)
            cur = a.right
        else:
            break

def preOrder(root):
    s = [root]
    while (len(s)):
        cur = s.pop()
        if cur:
            print(cur.data)
            s.append(cur.right)
            s.append(cur.left)

def postOrder(root):
    s = []
    justPopped = None
    cur = root
    while (True):
        while cur:
            s.append(cur)
            cur = cur.left
        #null now
        if len(s):
            temp = s[-1]
        else:
            break

        if temp.right and (temp.right != justPopped):
            cur = temp.right
        else:
            a = s.pop()
            justPopped = a
            print(a.data)

def in_order_parent(node):
    #initiate to left
    while node.left:
        node = node.left
    while node:
        print(node)
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node.parent.right is node:
                node = node.parent
            node = node.parent

def post_order_parent(node):
    #initiate to left
    while node.left:
        node = node.left
    while node:
        print(node)
        if node.parent and node.parent.right and node.parent.right is not node:
            node = node.parent.right
            while node.left or node.right:
                if node.left:
                    node = node.left
                else:
                    node = node.right
        else:
            node = node.parent

def pre_order_parent(node):
    while node:
        print(node)
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            while (node.parent):
                if (node.parent.right is None) or (node.parent.right is node):
                    node = node.parent
                else:
                    break
            if node.parent:
                node = node.parent.right
            else:
                node = None

if __name__ == '__main__':
    # Driver program to test above function

    """ Constructed binary tree is 
                1 
              /   \ 
             2     3 
           /  \ 
          4    5   """

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    a6 = Node(6)

    a1.parent = None
    a1.left = a2
    a1.right = a3
    a2.parent = a1
    a2.left = a4
    a2.right = a5
    a4.parent = a2
    a5.parent = a2
    a3.parent = a1
    a6.parent = a5
    a5.right = a6

    pre_order_parent(a1)