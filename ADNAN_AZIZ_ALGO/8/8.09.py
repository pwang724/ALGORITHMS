import LinkedList as LL

def get_k_last(ll, k):
    dummy = LL.Node('dummy')
    dummy.nextNode = ll.head

    kthNode = dummy
    endNode = dummy
    for i in range(k+1):
        endNode = endNode.nextNode
    while (endNode):
        endNode = endNode.nextNode
        kthNode = kthNode.nextNode
    ll.head = dummy.nextNode
    return kthNode, kthNode.nextNode

def rightshift(ll, k):
    if k == 0:
        return repr(ll)
    else:
        prev, cur = get_k_last(ll,k)
        end = ll.head
        while(end.nextNode):
            end = end.nextNode
        end.nextNode = ll.head
        prev.nextNode = None
        ll.head = cur
        end.nextNode = ll.head
    return repr(ll)

#allowing size to be used
def rightshift1(ll,k):
    last = ll.head
    n = 1
    while (last.nextNode):
        last = last.nextNode
        n+= 1
    last.nextNode = ll.head

    prev = None
    cur = ll.head
    for i in range(n-k):
        prev = cur
        cur = cur.nextNode
    ll.head = cur
    prev.nextNode = None
    return repr(ll)


if __name__ == '__main__':
    ll = LL.LinkedList()
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)
    print(rightshift1(ll,0))