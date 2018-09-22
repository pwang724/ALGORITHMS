from Node import Node

def height_balanced(node):
    def height(node):
        if node is None:
            return (True, -1)
        else:
            tup_l = height(node.left)
            tup_r = height(node.right)
            h = max(tup_l[1], tup_r[1]) + 1
            if abs(tup_l[1] - tup_r[1]) > 1:
                return (False, h)
            else:
                return (True, h)
    return height(node)[0]


if __name__ == '__main__':
    """ Constructed binary tree is 
                1 
              /   \ 
             2     3 
           /  \ 
          4    5   """

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)

    # a1.parent = None
    a1.left = a2
    a1.right = a3
    # a2.parent = a1
    a2.left = a4
    a2.right = a5
    # a4.parent = a2
    # a5.parent = a2
    # a3.parent = a1

    height_balanced(a1)