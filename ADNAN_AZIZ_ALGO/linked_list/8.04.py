import LinkedList as LL

def shared_node(ll_a, ll_b):
    def advance(ll, k):
        cur = ll.head
        for i in range(k):
            cur = cur.nextNode
        return cur

    s_a = ll_a.size()
    s_b = ll_b.size()
    if s_a > s_b:
        cur_a = advance(ll_a, s_a - s_b)
        cur_b = ll_b.head
    else:
        cur_a = ll_a.head
        cur_b = advance(ll_b, s_b - s_a)

    for i in range(min(s_a, s_b)):
        if cur_a == cur_b:
            return cur_a
        else:
            cur_a = cur_a.nextNode
            cur_b = cur_b.nextNode
    return False

if __name__ == '__main__':

    ll_a = LL.LinkedList()
    ll_b = LL.LinkedList()
    a = LL.Node('a')
    b = LL.Node('b')
    c = LL.Node('c')
    d = LL.Node('d')
    e = LL.Node('e')
    f = LL.Node('f')
    g = LL.Node('g')

    a.nextNode = b
    b.nextNode = c
    c.nextNode = d

    e.nextNode = f
    f.nextNode = g
    g.nextNode = c
    ll_a.head = a
    ll_b.head = e

    print(shared_node(ll_a, ll_b))

