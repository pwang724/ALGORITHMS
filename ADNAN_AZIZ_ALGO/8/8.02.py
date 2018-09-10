import LinkedList as LL

def reverse_subset(ll, a, b):
    prev = None
    cur = ll.head
    for i in range(1, a):
        prev = cur
        cur = cur.nextNode

    before_a = prev
    after_a = cur
    for i in range(a, b+1):
        next = cur.nextNode
        cur.nextNode = prev
        prev = cur
        cur = next
    before_b = prev
    after_b = cur

    before_a.nextNode = before_b
    after_a.nextNode = after_b

    return repr(ll)

if __name__ == '__main__':
    ll = LL.LinkedList()
    ll.push(2)
    ll.push(7)
    ll.push(5)
    ll.push(3)
    ll.push(11)

    print(ll)
    print(reverse_subset(ll,2,4))





