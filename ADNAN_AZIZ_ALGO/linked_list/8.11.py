import LinkedList as LL

#time complexity n, space complexity n
def palindromic(ll):
    l = []
    cur = ll.head
    while (cur):
        l.append(cur.data)
        cur = cur.nextNode
    i = 0
    j = len(l)-1
    while (i < j):
        if l[i] != l[j]:
            return False
        i+= 1
        j-= 1
    return True

def reverse_subset(ll, b):
    prev = None
    cur = ll.head
    for i in range(b):
        next = cur.nextNode
        cur.nextNode = prev
        prev = cur
        cur = next
    return prev, cur

#time complexity n, space complexity 1
def palindromic1(ll):
    n = 0
    cur = ll.head
    while (cur):
        n+= 1
        cur = cur.nextNode

    rem = n %2
    k = n/2
    start_cur, end_cur = reverse_subset(ll, k)
    if rem:
        end_cur = end_cur.nextNode

    while (start_cur):
        if start_cur.data != end_cur.data:
            return False
        start_cur = start_cur.nextNode
        end_cur = end_cur.nextNode
    return True



if __name__ == '__main__':
    ll = LL.LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    print(palindromic1(ll))