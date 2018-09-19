import Stack_List as Stack

def well_formed(str):
    newstk = Stack.Stack()

    for cur in str:
        if cur == '[' or cur == '(' or cur == '{':
            newstk.push(cur)
        else:
            if not newstk.size():
                return False
            else:
                left_brace = newstk.pop()
                if (left_brace == '{' and cur != '}') or \
                    (left_brace == '[' and cur != ']') or \
                    (left_brace == '(' and cur != ')'):
                    return False
    return True






if __name__ == '__main__':
    print(well_formed('[({})]'))
    print(well_formed('()[]{[]}{[][]([])}'))
    print(well_formed('())'))