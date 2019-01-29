import LinkedList as LL

def deleteNode(node):
    node.data = node.nextNode.data
    node.nextNode = node.nextNode.nextNode

def remove_k_last(ll, k):
    dummy = LL.Node('dummy')
    dummy.nextNode = ll.head

    kthNode = dummy
    endNode = dummy
    for i in range(k+1):
        endNode = endNode.nextNode
    while (endNode):
        endNode = endNode.nextNode
        kthNode = kthNode.nextNode
    kthNode.nextNode = kthNode.nextNode.nextNode
    ll.head = dummy.nextNode
    return repr(ll)

if __name__ == '__main__':
    #test cases: shared/not shared for non cycles, 1 cycle 1 not, and 2 cycles
    a = LL.Node('a')
    b = LL.Node('b')
    c = LL.Node('c')
    d = LL.Node('d')

    ll = LL.LinkedList()
    # a.nextNode = b
    # b.nextNode = c
    # c.nextNode = d
    ll.head = a

    remove_k_last(ll,1)
    print(ll)