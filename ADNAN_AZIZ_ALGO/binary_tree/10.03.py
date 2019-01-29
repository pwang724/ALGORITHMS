from Node import Node

def LCA(node, a, b):
    if node is None:
        return (0, None)
    else:
        temp = 0
        if node.data == a or node.data == b:
            temp = 1

        l = LCA(node.left, a, b)
        r = LCA(node.right, a, b)
        if (l[0] + r[0] + temp) > 1:
            return (1, node)
        elif l[1]:
            return l
        elif r[1]:
            return r
        else:
            return (l[0]+r[0] + temp, None)

if __name__ == '__main__':
    p = Node('p', None, None)
    o = Node('o', None, p)
    n = Node('n')
    m = Node('m')
    l = Node('l', None, m)
    k = Node('k', l, n)
    j = Node('j', None, k)
    i = Node('i', j, o)

    h = Node('h')
    g = Node('g', h)
    f = Node('f', None, g)
    e = Node('e')
    d = Node('d')
    c = Node('c', d, e)
    b = Node('b', c, f)
    a = Node('a', b, i)

    print(LCA(a,'l','p'))

    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \
    #       4    5   """
    #
    # a1 = Node(1)
    # a2 = Node(2)
    # a3 = Node(3)
    # a4 = Node(4)
    # a5 = Node(5)
    #
    # # a1.parent = None
    # a1.left = a2
    # a1.right = a3
    # # a2.parent = a1
    # a2.left = a4
    # a2.right = a5
    # # a4.parent = a2
    # # a5.parent = a2
    # # a3.parent = a1
    #
    # print(LCA(a1, 2, 5))