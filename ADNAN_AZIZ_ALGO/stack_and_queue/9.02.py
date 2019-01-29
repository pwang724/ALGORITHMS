import Stack_List as Stack


def process(str):
    stk = Stack.Stack()
    l = len(str)
    i = 0
    while (i < l):
        if str[i].isdigit() or str[i] == '-':
            val = 0
            sign = 1
            if str[i] == '-':
                sign = -1
                i+= 1
            while(str[i].isdigit()):
                val = val * 10 + int(str[i])
                i += 1
            stk.push(sign * val)
            i+= 1
        else:
            stk.push(str[i])
            i+= 2
    return stk

def rpn(str):
    def helper(stack):
        thing = stack.pop()
        if thing == '+':
            return stack.pop() + helper(stack)
        elif thing == '-':
            return stack.pop() - helper(stack)
        elif thing == '/':
            return stack.pop() / helper(stack)
        elif thing == 'x':
            return stack.pop() * helper(stack)
        else:
            return thing
    stack = process(str)
    return helper(stack)


if __name__ == '__main__':
    print(rpn('3,4,+,2,x,-1,+'))