from Node import Node

def LCA(a, b):
    def height(node):
        i = 0
        while (node):
            node = node.parent
            i+= 1
        return i

    def move_up(node, n):
        for i in range(n):
            node = node.parent
        return node

    h_a = height(a)
    h_b = height(b)
    diff = h_a - h_b
    if diff > 0:
        a = move_up(a, diff)
    else:
        b = move_up(b, -diff)

    for i in range(min(h_a, h_b)):
        if a is b:
            return a
        else:
            a = a.parent
            b = b.parent
    return None





if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \
    #       4    5   """

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

    print(LCA(a2, a5))