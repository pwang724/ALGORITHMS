import LinkedList as LL

def cycle_hash(ll):
    cur = ll.head
    dict = {}
    while (cur):
        if id(cur) in dict:
            return True
        else:
            dict[id(cur)] = '1'
    return False

def cycle_loops(ll):
    cur = ll.head
    total = 2
    while (cur):
        comp = ll.head
        count = 0
        visited = 0
        while (comp and total > count):
            if comp == cur:
                visited += 1
                if visited > 1:
                    return True
            comp = comp.nextNode
            count += 1
        cur = cur.nextNode
        total += 2
    return False

def cycle_iter(ll):
    slow = ll.head
    fast = ll.head
    cycle_bool = 0
    while (slow and cycle_bool == 0):
        for i in range(2):
            fast = fast.nextNode
            if fast == None:
                return False
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
        return repr(slow)


if __name__ == '__main__':

    ll = LL.LinkedList()
    a = LL.Node('a')
    b = LL.Node('b')
    c = LL.Node('c')
    d = LL.Node('d')

    a.nextNode = b
    b.nextNode = c
    c.nextNode = d
    d.nextNode = c
    ll.head = a

    print(cycle_iter(ll))

