import LinkedList as LL

def unique(ll):
    cur = ll.head
    dup = cur.data
    while (cur.nextNode):
        next = cur.nextNode
        if dup == next.data:
            cur.nextNode = next.nextNode
        else:
            dup = cur.nextNode.data
            cur = cur.nextNode
    return repr(ll)

#better solution because it doesn't have to go through outer loop every time
#to delete a duplicate value. useful if outer loop is big / has lot of conditions
def unique1(ll):
    cur = ll.head
    while (cur):
        next = cur.nextNode
        while (next and next.data == cur.data):
            cur.nextNode = next.nextNode
            next = cur.nextNode
        cur = cur.nextNode
    return repr(ll)

if __name__ == '__main__':
    ll = LL.LinkedList()
    ll.push(10)
    ll.push(9)
    ll.push(9)
    ll.push(8)
    ll.push(7)
    ll.push(5)
    ll.push(1)
    ll.push(1)
    ll.push(1)
    print(unique1(ll))