from Node import Node

def inorder_iter(node):
    stack = []
    cur = node
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            if stack:
                cur = stack.pop()
                print(cur)
                cur = cur.right
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
    #            7   linked_list"""

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

    inorder_iter(a1)