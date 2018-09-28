from Node import Node
from TreeTraversal_iter import inOrder, preOrder
def make_from_order(in_order, pre_order):
    _dict = {str:i for i, str in enumerate(in_order)}
    l = len(in_order)


    def helper(in_start, in_end, pre_start, pre_end):
        if in_start >= in_end and pre_start >= pre_end:
            return None
        else:
            chr = pre_order[pre_start]
            root = Node(chr)
            i = _dict[chr]
            left_size = i - in_start


            in_left_start = in_start
            in_left_end = i
            pre_left_start = pre_start + 1
            pre_left_end = pre_start + left_size + 1
            in_right_start = i+1
            in_right_end = in_end
            pre_right_start = pre_start + left_size + 1
            pre_right_end = pre_end

            root.left = helper(in_left_start, in_left_end, pre_left_start, pre_left_end)
            root.right = helper(in_right_start, in_right_end, pre_right_start, pre_right_end)
            # root.left = helper(in_start, i, pre_start+1, i+1)
            # root.right = helper(i+1, l, i+1, l)
            return root
    return helper(0, l, 0, l)


if __name__ == '__main__':
    in_order = ['F','B','A','E','H','C','D','I','G']
    pre_order = ['H','B','F','E','A','C','D','G','I']

    root = make_from_order(in_order, pre_order)
    inOrder(root)
    print('space')
    preOrder(root)
