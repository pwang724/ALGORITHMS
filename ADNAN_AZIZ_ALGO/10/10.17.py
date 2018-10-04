def lock(node):
    #if can be locked, lock it and return true
    #if cant be locked, return false

    #see if any parent node is locked, including own
    parent_lock = False
    cur_node = node
    while(not parent_lock and cur_node):
        parent_lock = cur_node.lock
        cur_node = cur_node.parent

    #see if any descendant node is locked, including own
    def helper(node):
        if not node:
            return False
        return node.lock or helper(node.left) or helper(node.right)
    descendant_lock = helper(node)

    can_lock = not (parent_lock or descendant_lock)
    if can_lock:
        node.lock = True
    return can_lock

def is_locked(node):
    return node.lock

def unlock(node):
    node.lock = False