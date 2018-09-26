from Node import Node

def preorder_iter(node):
    stack = []
    stack.append(node)
    while stack:
        cur = stack.pop()
        if cur:
            print(cur)
            stack.append(cur.right)
            stack.append(cur.left)

def postorder_iter(node):
    stack = []
    cur = node
    justPopped = None
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            if stack:
                temp = stack[-1]
                if temp.right and temp.right is not justPopped:
                    cur = temp.right
                else:
                    justPopped = stack.pop()
                    print(justPopped)
            else:
                return 'done'

if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \
    #       4    5
    #             \
    #              6
    #             / \
    #            7   8"""

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    a6 = Node(6)
    a7 = Node(7)
    a8 = Node(8)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a5.right = a6
    a6.left = a7
    a6.right = a8

    preorder_iter(a1)