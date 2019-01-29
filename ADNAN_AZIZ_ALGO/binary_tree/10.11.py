from Node import Node

def inorder_parent(node):
    while (node.left):
        node = node.left

    while (node):
        print(node)
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node is node.parent.right:
                node = node.parent
            node = node.parent



if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \
    #       4    5
    #             \
    #              6
    #             / \
    #            7   linked_list"""

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    a6 = Node(6)
    a7 = Node(7)
    a8 = Node(8)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5

    a1.parent = None
    a2.parent = a1
    a4.parent = a2
    a5.parent = a2
    a3.parent = a1
    a6.parent = a5
    a7.parent = a6
    a8.parent = a6

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a5.right = a6
    a6.left = a7
    a6.right = a8

    print(inorder_parent(a1))