from Stack_List import Stack

def sunset_view(l):
    stack = Stack()
    id = 0
    while (len(l)):
        cur = l.pop()
        while (stack.size() and cur >= stack.peek()[0]):
            stack.pop()
        stack.push([cur, id])
        id +=1

    id_stack = Stack()
    while (stack.size()):
        a = stack.pop()
        id_stack.push(a[1])

    return id_stack

if __name__ == '__main__':
    l = [3,1,5,3,7,9,7,3,1]
    print(sunset_view(l))