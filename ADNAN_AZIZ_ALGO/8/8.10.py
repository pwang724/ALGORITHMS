import LinkedList as LL

def even_odd(ll):
    dummyhead = LL.Node('dummy')
    dummyhead.nextNode = ll.head
    even = dummyhead
    odd = ll.head

    while (True):
        if odd.nextNode:
            even.nextNode = odd.nextNode
            even = even.nextNode
        else:
            even.nextNode = ll.head
            ll.head = dummyhead.nextNode
            return repr(ll)

        if even.nextNode:
            odd.nextNode = even.nextNode
            odd = odd.nextNode
        else:
            odd.nextNode = None
            even.nextNode = ll.head
            ll.head = dummyhead.nextNode
            return repr(ll)

def even_odd1(ll):
    dummyhead = LL.Node('dummy')
    dummyhead.nextNode = ll.head
    even = dummyhead
    odd = ll.head

    while (True):
        if odd.nextNode:
            even.nextNode = odd.nextNode
            even = even.nextNode
        else:
            even.nextNode = ll.head
            ll.head = dummyhead.nextNode
            return repr(ll)

        if even.nextNode:
            odd.nextNode = even.nextNode
            odd = odd.nextNode
        else:
            odd.nextNode = None
            even.nextNode = ll.head
            ll.head = dummyhead.nextNode
            return repr(ll)




if __name__ == '__main__':
    ll = LL.LinkedList()
    # ll.push(5)
    # ll.push(4)
    # ll.push(3)
    # ll.push(2)
    ll.push(1)
    print(even_odd(ll))