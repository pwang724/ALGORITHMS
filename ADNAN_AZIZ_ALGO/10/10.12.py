from Node import Node
from TreeTraversal_iter import inOrder, preOrder
def make_from_order(in_order, pre_order):
    if not(in_order) and not(pre_order):
        return None
    else:
        chr = pre_order.pop(0)
        root = Node(chr)
        i = 0
        while in_order[i] != chr:
            i+=1

        root.left = make_from_order(in_order[:i], pre_order[:i])
        root.right = make_from_order(in_order[i+1:], pre_order[i:])
    return root







if __name__ == '__main__':
    in_order = ['F','B','A','E','H','C','D','I','G']
    pre_order = ['H','B','F','E','A','C','D','G','I']

    root = make_from_order(in_order, pre_order)
    inOrder(root)
    print('space')
    preOrder(root)
