import LinkedList as LL

def deleteNode(node):
    node.data = node.nextNode.data
    node.nextNode = node.nextNode.nextNode

if __name__ == '__main__':
    #test cases: shared/not shared for non cycles, 1 cycle 1 not, and 2 cycles
    a = LL.Node('a')
    b = LL.Node('b')
    c = LL.Node('c')
    d = LL.Node('d')

    ll = LL.LinkedList()
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = None
    ll.head = a

    deleteNode(c)
    print(ll)