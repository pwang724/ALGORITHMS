import LinkedList as LL

def cycle_iter(ll):
    slow = ll.head
    fast = ll.head
    cycle_bool = 0
    while (slow and cycle_bool == 0):
        for i in range(2):
            fast = fast.nextNode
            if fast == None:
                return None, 0
            elif fast == slow:
                cycle_bool = 1
        slow = slow.nextNode

    if cycle_bool:
        cycle_length = 1
        fast = slow.nextNode
        while (fast != slow):
            fast = fast.nextNode
            cycle_length += 1

        fast = ll.head
        slow = ll.head
        for i in range(cycle_length):
            fast = fast.nextNode

        while (slow != fast):
            slow = slow.nextNode
            fast = fast.nextNode
        return slow, cycle_length

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

def cycle_shared_node(ll_a, ll_b):
    a_cycle, a_length = cycle_iter(ll_a)
    b_cycle, b_length = cycle_iter(ll_b)

    if not a_length and not b_length:
        return shared_node(ll_a, ll_b)
    elif a_length != b_length:
            return False
    else:
        #test if shared is before cycle starts
        old_a = a_cycle.nextNode
        old_b = b_cycle.nextNode
        a_cycle.nextNode = None
        b_cycle.nextNode = None
        shared_before_cycle = shared_node(ll_a, ll_b)
        if shared_before_cycle:
            return shared_before_cycle
        else:
            a_cycle.nextNode = old_a
            b_cycle.nextNode = old_b
            for i in range(b_length):
                if b_cycle == a_cycle:
                    return a_cycle
                b_cycle = b_cycle.nextNode
            return False

if __name__ == '__main__':
    #test cases: shared/not shared for non cycles, 1 cycle 1 not, and 2 cycles
    a = LL.Node('a')
    b = LL.Node('b')
    c = LL.Node('c')
    d = LL.Node('d')
    e = LL.Node('d')
    f = LL.Node('f')
    g = LL.Node('g')
    h = LL.Node('h')

    ll_a = LL.LinkedList()
    ll_b = LL.LinkedList()

    #cycle no shared node
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = b
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = f
    ll_b.head = f
    # print(cycle_shared_node(ll_a, ll_b))

    #cycle shared node after cycle
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = b
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = c
    ll_b.head = f
    # print(cycle_shared_node(ll_a, ll_b))

    #cycle shared node before cycle
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = c
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = b
    ll_b.head = f
    print(cycle_shared_node(ll_a, ll_b))

    #cycle and no cycle
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = b
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = None
    ll_b.head = f
    # print(cycle_shared_node(ll_a, ll_b))

    #two no cycles and no shared
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = None
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = None
    ll_b.head = f
    # print(cycle_shared_node(ll_a, ll_b))

    #two no cycles and shared
    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = None
    ll_a.head = a

    e.nextNode = f
    f.nextNode = g
    g.nextNode = h
    h.nextNode = b
    ll_b.head = f
    # print(cycle_shared_node(ll_a, ll_b))

