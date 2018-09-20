import Queue_List
from BinaryTree import BinaryTreeNode

def breadth_first_search(first_node):
    q = Queue_List.Queue()

    if first_node:
        q.enqueue(first_node)
    else:
        return 'nothing'

    out = []
    while (True):
        l = []
        temp = Queue_List.Queue()

        if not q.size():
            return out

        while (q.size()):
            node = q.dequeue()
            l.append(node.data)

            if node.left:
                temp.enqueue(node.left)
            if node.right:
                temp.enqueue(node.right)
        out.append(l)
        q = temp

if __name__ == '__main__':
    z = BinaryTreeNode(28, None, None)
    e = BinaryTreeNode(271, z, None)
    f = BinaryTreeNode(561, None, None)
    g = BinaryTreeNode(2, None, None)

    b = BinaryTreeNode(5, e, f)
    c = BinaryTreeNode(6, g, None)
    a = BinaryTreeNode(314, b, c)

    print(breadth_first_search(a))


