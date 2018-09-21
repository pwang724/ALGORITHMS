from BinaryTree import BinaryTree

def TreeTraversal(node):
    # pre order
    if node:
        print(node.data)
        TreeTraversal(node.left)
        TreeTraversal(node.right)

    # # in order
    # if node:
    #     TreeTraversal(node.left)
    #     print(node.data)
    #     TreeTraversal(node.right)

    # #post order
    # if node:
    #     TreeTraversal(node.left)
    #     TreeTraversal(node.right)
    #     print(node.data)

def TreeTraversal_iter(node):
    a = []
    traversed = []
    a.append(node)
    traversed.append(node)

    #in order
    while (a):
        cur = a.pop()
        if ((not cur.left or cur.left in traversed) and (not cur.right or cur.right in traversed)):
            print(cur.data)
        else:
            if (cur.right not in traversed and cur.right):
                a.append(cur.right)
                traversed.append(cur.right)

            if (cur.left not in traversed and cur.left):
                a.append(cur.left)
                traversed.append(cur.left)
            a.append(cur)

def pre_order(node):
    a = []
    a.append(node)

    while (a):
        cur = a.pop()
        print(cur.data)
        if cur.right:
            a.append(cur.right)
        if cur.left:
            a.append(cur.left)


if __name__ == '__main__':
    p = BinaryTree('p', None, None)
    o = BinaryTree('o', None, p)
    n = BinaryTree('n')
    m = BinaryTree('m')
    l = BinaryTree('l', None, m)
    k = BinaryTree('k', l, n)
    j = BinaryTree('j', None, k)
    i = BinaryTree('i', j, o)

    h = BinaryTree('h')
    g = BinaryTree('g', h)
    f = BinaryTree('f', None, g)
    e = BinaryTree('e')
    d = BinaryTree('d')
    c = BinaryTree('c', d, e)
    b = BinaryTree('b', c, f)
    a = BinaryTree('a', b, i)

    pre_order(a)
