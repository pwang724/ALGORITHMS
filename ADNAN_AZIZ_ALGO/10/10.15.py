from Node import Node

def compute_exterior(node):
    a = []
    first_node = node
    def helper_leaves(node):
        if node:
            if not node.left and not node.right:
                a.append(node)
            else:
                helper_leaves(node.left)
                helper_leaves(node.right)

    def helper_left(node):
        while True:
            a.append(node)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                break

    def helper_right(node):
        if node.right:
            helper_right(node.right)
        elif node.left:
            helper_right(node.left)
        a.append(node)

    helper_left(first_node)
    a.pop()

    helper_leaves(first_node)
    a.pop()

    helper_right(first_node)
    a.pop()
    return a

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

    print(compute_exterior(a))

    # abcdehmnpoi