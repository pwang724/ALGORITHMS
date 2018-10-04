from Node import Node
from LinkedList import LinkedList
import TreeTraversal_iter

def makeLL(node):
    a = LinkedList()

    def helper(node):
        if node:
            if not node.left and not node.right:
                a.push(node)
            else:
                #adding lists from right to left because have to push the head (stack, lifo)
                #otherwise the next two lines would be reversed
                helper(node.right)
                helper(node.left)
    helper(node)
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

    print(TreeTraversal_iter.preOrder(a))
    ll = makeLL(a)
    print(ll)

# efgijmno