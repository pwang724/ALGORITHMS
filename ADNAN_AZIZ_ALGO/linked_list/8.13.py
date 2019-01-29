import linked_list.LinkedList as LL

def add(ll_a, ll_b):
    cur_a = ll_a.head
    cur_b = ll_b.head
    carry = 0
    cur = LL.Node('dummy')
    cur_start = cur
    ll = LL.LinkedList()

    while (cur_a or cur_b):
        if cur_a and cur_b:
            sum = cur_a.data + cur_b.data
            cur_a = cur_a.nextNode
            cur_b = cur_b.nextNode
        elif cur_a and not cur_b:
            sum = cur_a.data
            cur_a = cur_a.nextNode
        else:
            sum = cur_b
        sum += carry
        val = sum % 10
        carry = sum / 10
        cur.nextNode = LL.Node(val)
        cur = cur.nextNode

    if carry:
        cur.nextNode = LL.Node(carry)

    ll.head = cur_start.nextNode
    return repr(ll)




if __name__ == '__main__':
    ll_a = LL.LinkedList()
    ll_a.push(9)
    ll_a.push(9)
    ll_a.push(9)

    ll_b = LL.LinkedList()
    ll_b.push(1)
    # ll_b.push(0)
    # ll_b.push(7)
    print(ll_a)
    print(ll_b)
    print(add(ll_a, ll_b))