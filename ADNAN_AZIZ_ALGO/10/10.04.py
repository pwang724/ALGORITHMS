from Node import Node

def LCA(node, a, b):
    def helper(node, a):
        l = []
        while (node.left):
            node = node.left

        while (node):
            if a == node.data:
                while (node):
                    l.append(node.data)
                    node = node.parent
                return l
            if node.parent and node.parent.right and node.parent.right is not node:
                node = node.parent.right
                while (node.left or node.right):
                    if node.left:
                        node = node.left
                    else:
                        node = node.right
            else:
                node = node.parent
    l1 = helper(node, a)
    l2 = helper(node, b)
    diff = len(l2) - len(l1)
    if diff > 0:
        l2 = l2[diff:]
    else:
        l1 = l1[-diff:]

    for a, b in zip(l1, l2):
        if a == b:
            return a
    return None


if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \
    #       4    5   """

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)

    a1.parent = None
    a1.left = a2
    a1.right = a3
    a2.parent = a1
    a2.left = a4
    a2.right = a5
    a4.parent = a2
    a5.parent = a2
    a3.parent = a1

    print(LCA(a1, 4, 3))