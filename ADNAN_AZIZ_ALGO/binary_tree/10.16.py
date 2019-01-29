import TreeTraversal_iter

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        self.locked = False
        self.num_de_locked = 0

    def __repr__(self):
        return repr(self.data)

def is_locked(node):
    return node.locked

def lock(node):
    if node.locked:
        return 'already locked'
    else:
        descendants_locked = node.num_de_locked > 0
        parents_locked = False
        cur = node
        while (not parents_locked and cur):
            parents_locked = cur.locked
            cur = cur.parent

        if not (descendants_locked or parents_locked):
            node.locked = True
            cur = node
            while (cur):
                cur.num_de_locked += 1
                cur = cur.parent
            return True
        else:
            return False

def unlock(node):
    if not node.locked:
        return
    else:
        node.locked = False
        cur = node
        while (cur):
            cur.num_de_locked -= 1
            cur = cur.parent

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

    print(TreeTraversal_iter.preOrder(a))
