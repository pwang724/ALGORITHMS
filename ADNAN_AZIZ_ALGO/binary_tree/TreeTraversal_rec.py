from binary_tree.Node import Node

def TreeTraversal(node):
    # pre order
    # if node:
    #     print(node.data)
    #     TreeTraversal(node.left)
    #     TreeTraversal(node.right)

    # # in order
    # if node:
    #     TreeTraversal(node.left)
    #     print(node.data)
    #     TreeTraversal(node.right)

    #post order
    if node:
        TreeTraversal(node.left)
        TreeTraversal(node.right)
        print(node.data)


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

    TreeTraversal(a)
