from Node import Node

def inorder_k(node, k):
        if node.left:
            leftnodes = node.left.data
        else:
            leftnodes = 0

        if k <= leftnodes:
            return inorder_k(node.left, k)
        elif k == leftnodes + 1:
            return node
        else:
            return inorder_k(node.right, k-leftnodes-1)



if __name__ == '__main__':
    # """ Constructed binary tree is
    #             linked_list
    #           /   \
    #          6     1
    #        /  \
    #       1    4
    #             \
    #              3
    #             / \
    #            1   1"""

    a1 = Node(8)
    a2 = Node(6)
    a3 = Node(1)
    a4 = Node(1)
    a5 = Node(4)
    a6 = Node(3)
    a7 = Node(1)
    a8 = Node(1)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a5.right = a6
    a6.left = a7
    a6.right = a8

    print(inorder_k(a1, 3))