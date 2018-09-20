import Stack_List as Stack

def postings_list_r(ll):
    def helper(node):
        if node is not None and node.order == -1:
            helper(node.jump)
            helper(node.nextNode)
    helper(ll.head)

def postings_list_i(ll):
    stack = Stack.Stack()
    stack.push(ll.head)
    order = 0
    while (stack.size()):
        cur = stack.pop()

        if cur.order == -1 and cur is not None:
            cur.order = order
            order += 1
            stack.push(cur.nextNode)
            stack.push(cur.jump)





