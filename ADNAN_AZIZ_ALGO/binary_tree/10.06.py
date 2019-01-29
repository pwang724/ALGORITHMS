from Node import Node

def contains_sum(node, val):
    def helper(node, tup, sum):
        if node is None:
            return tup
        else:
            cur_sum = node.data + tup[0]
            if cur_sum == sum:
                return (cur_sum, True)
            else:
                new_tup = (cur_sum, False)

                tup_l = helper(node.left, new_tup, sum)
                if tup_l[1]:
                    return (sum, True)

                tup_r = helper(node.right, new_tup, sum)
                if tup_r[1]:
                    return (sum, True)

                else:
                    return new_tup
    return helper(node, (0, False), val)


def contains_sum_(node, cur_sum):
        if node is None:
            return False
        cur_sum = cur_sum - node.data
        if node.left == None and node.right == None:
            return cur_sum == 0
        elif cur_sum > 0:
            return contains_sum_(node.left, cur_sum) or contains_sum_(node.right, cur_sum)
        else:
            return False

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
    a5.right = a6
    a6.left = a7
    a6.right = a8

    a1.parent = None
    a1.left = a2
    a1.right = a3
    a2.parent = a1
    a2.left = a4
    a2.right = a5
    a4.parent = a2
    a5.parent = a2
    a3.parent = a1

    print(contains_sum_(a1, 4))

