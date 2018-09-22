from Node import Node

def symmetric_tree(node):
    a = node.left
    b = node.right

    def symmetric(a, b):
        if (a is None) and (b is None):
            return True
        elif bool(a) ^ bool(b):
            return False
        else:
            boo = a.data == b.data
            boo_left = symmetric(a.left, b.left)
            boo_right = symmetric(a.right, b.right)
            return boo_left and boo_right and boo
    return symmetric(a,b)

if __name__ == '__main__':
    """ Constructed binary tree is 
                1 
              /   \ 
             2     2 
           /  \ 
          3    4   """

    a1 = Node(1)
    a2 = Node(2)
    a2_ = Node(2)
    a3 = Node(3)
    a3_ = Node(3)
    a4 = Node(4)
    a4_ = Node(4)

    a1.left = a2
    a1.right = a2_
    a2.left = a3
    # a2.right = a4
    a2_.left = a3_
    # a2_.right = a4_

    print(symmetric_tree(a1))

