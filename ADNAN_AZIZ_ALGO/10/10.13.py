from Node import Node
from LinkedList import LinkedList
import TreeTraversal_iter

def pre_order_make(l):
    str = l.pop(0)
    if str is None:
        return None
    else:
        node = Node(str)
        NoneCount = 0
        ValidCount = 0
        i = 0
        while (i < len(l) and ValidCount >= NoneCount):
            if l[i]:
                ValidCount += 1
            else:
                NoneCount += 1
            i+= 1
        node.left = pre_order_make(l[:i])
        node.right = pre_order_make(l[i:])
        return node

def reconstruct_preorder(preorder):
    subtree_key = preorder.pop(0)
    if subtree_key is None:
        return None

    # Note that reconstruct_preorder_helper updates preorder_iter. So the
    # order of following two calls are critical.
    left_subtree = reconstruct_preorder(preorder)
    right_subtree = reconstruct_preorder(preorder)
    return Node(subtree_key, left_subtree, right_subtree)


if __name__ == '__main__':
    l = ['H','B','F', None, None, 'E','A', None, None, None, 'C', None, 'D',
         None, 'G','I', None, None, None]
    l = ['A','B',None,None,'C',None,None]
    a = reconstruct_preorder(l)
    TreeTraversal_iter.preOrder(a)
