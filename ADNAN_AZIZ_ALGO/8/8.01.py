import LinkedList as LL

def merge(ll_i, ll_j):
    # can be simplified by using a dummy head = new Node. then set head as dummy.nextNode
    if ll_i.head.data <= ll_j.head.data:
        cur = ll_i.head
        node_i = ll_i.head.nextNode
        node_j = ll_j.head
        head = ll_i
    else:
        cur = ll_j.head
        node_i = ll_i.head
        node_j = ll_j.head.nextNode
        head = ll_j

    while (node_i and node_j):
        if node_i.data >= node_j.data:
            cur.nextNode = node_j
            node_j = node_j.nextNode
        else:
            cur.nextNode = node_i
            node_i = node_i.nextNode
        cur = cur.nextNode

    if (node_i):
        cur.nextNode = node_i
    else:
        cur.nextNode = node_j
    return repr(head)

if __name__ == '__main__':

    ll_a = LL.LinkedList()
    ll_a.push(10)
    ll_a.push(8)
    ll_a.push(6)
    ll_a.push(4)
    ll_a.push(2)

    ll_b = LL.LinkedList()
    ll_b.push(7)
    ll_b.push(5)
    ll_b.push(3)
    ll_b.push(1)

    print(merge(ll_a, ll_b))



