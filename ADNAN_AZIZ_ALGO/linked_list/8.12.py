import LinkedList as LL

#time complexity n
def pivot(ll,k):
    lower_head = LL.Node('dummy')
    equal_head = LL.Node('dummy')
    higher_head = LL.Node('dummy')
    lower = lower_head
    equal = equal_head
    higher = higher_head

    cur = ll.head
    while (cur):
        if cur.data < k:
            lower.nextNode = cur
            lower = lower.nextNode
        elif cur.data == k:
            equal.nextNode = cur
            equal = equal.nextNode
        else:
            higher.nextNode = cur
            higher = higher.nextNode
        cur = cur.nextNode
    higher.nextNode = None
    lower.nextNode = equal_head.nextNode
    equal.nextNode = higher_head.nextNode
    ll.head = lower_head.nextNode
    return repr(ll)


if __name__ == '__main__':
    ll = LL.LinkedList()
    ll.push(1)
    ll.push(8)
    ll.push(3)
    ll.push(7)
    ll.push(5)
    ll.push(4)
    ll.push(10)
    ll.push(2)
    ll.push(6)
    print(ll)
    print(pivot(ll,6))