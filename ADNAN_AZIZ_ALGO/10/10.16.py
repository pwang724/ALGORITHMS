class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.level_next = None

    def __repr__(self):
        return repr(self.data)

def set_level_next(node):
    if node:
        if node.left and node.right:
            node.left.level_next = node.right
            if node.level_next:
                node.right.level_next = node.level_next.left

        set_level_next(node.left)
        set_level_next(node.right)

def level_next_print(node):
    if node:
        print([node.data, node.level_next])
        level_next_print(node.left)
        level_next_print(node.right)


if __name__ == '__main__':
    # """ Constructed binary tree is
    #             1
    #           /   \
    #          2     3
    #        /  \   / \
    #       4    5 6   7

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    a6 = Node(6)
    a7 = Node(7)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a2.right = a5
    a3.left = a6
    a3.right = a7

    set_level_next(a1)
    level_next_print(a1)
