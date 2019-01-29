from Node import Node

def sum_root_to_leaf(node):
    def helper(node, sum):
        cur = sum * 2 + node.data
        if not node.left and not node.right:
            return cur
        else:
            l = 0
            r = 0
            if node.left:
                l = helper(node.left, cur)
            if node.right:
                r = helper(node.right, cur)
        return l + r
    return helper(node, 0)


if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          0     1
    #        /  \
    #       1    0
    #             \
    #              1
    #             / \
    #            1   0"""

    a1 = Node(1)
    a2 = Node(0)
    a3 = Node(1)
    a4 = Node(1)
    a5 = Node(0)
    a6 = Node(1)
    a7 = Node(1)
    a8 = Node(0)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a5.right = a6
    a6.left = a7
    a6.right = a8

    print(sum_root_to_leaf(a1))