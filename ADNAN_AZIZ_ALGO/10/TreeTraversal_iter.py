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

def postOrder_parent(root):
    cur = root
    while (True):
        if cur.left and not cur.left.done:
            cur = cur.left
        elif cur.right and not cur.right.done:
            cur = cur.right
        else:
            print(cur)
            cur.done = True
            if cur.parent:
                cur = cur.parent
            else:
                break

def inOrder_parent(root):
    cur = root
    while (True):
        if cur.left and not cur.left.done:
            cur = cur.left
        elif not cur.done:
            print(cur)
            cur.done = True
            if cur.right and not cur.right.done:
                cur = cur.right
        else:
            if cur.parent:
                cur = cur.parent
            else:
                break

def preOrder_parent(root):
    cur = root
    while (True):
        if not cur.done:
            print(cur)
            cur.done = True
        elif cur.done:
            if cur.left and not cur.left.done:
                cur = cur.left
            elif cur.right and not cur.right.done:
                cur = cur.right
            else:
                if cur.parent:
                    cur = cur.parent
                else:
                    break

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

a1.parent = None
a1.left = a2
a1.right = a3
a2.parent = a1
a2.left = a4
a2.right = a5
a4.parent = a2
a5.parent = a2
a3.parent = a1

preOrder_parent(a1)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)