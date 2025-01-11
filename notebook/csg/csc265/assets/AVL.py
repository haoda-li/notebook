class AVLNode:
    # Constructor to create a new node
    def __init__(self, key):
        self.k = key
        self.l = None
        self.r = None
        self.parent = None
        self.height = 0

get_height = lambda node: -1 if node is None else node.height
def get_BF(node):
    if node is None:
        return 0
    rh = get_height(node.r)
    lh = get_height(node.l)
    return rh - lh

# to better trace the result, we will use 
# iterative method to implement BST insert
# and obtain the newly created node
def BST_insert(root, k):
    new_node = AVLNode(k)
    if root is None:
        return new_node
    parent, curr = None, root
    while curr:
        parent = curr
        if k < curr.k:
            curr = curr.l
        else:
            curr = curr.r
    new_node.parent = parent
    if k < parent.k:
        parent.l = new_node
    else:
        parent.r = new_node
    return new_node
        
def BST_update_height(new_node):
    curr = new_node.parent
    while curr is not None:
        rh = get_height(curr.r)
        lh = get_height(curr.l)
        curr.height = max(rh, lh) + 1
        curr = curr.parent

def fix_imbalance(new_node):
    curr = new_node.parent
    # fix according to BF
    while curr is not None:
        bf = get_BF(curr)
        if bf == 0:
            curr.height = max(get_height(curr.l), get_height(curr.r)) + 1
            return
        if bf == -2:
            if get_height(curr.l.l) == get_height(curr.r) + 1:
                left_rotate(curr)
            else:
                right_rotate(curr.l)
                left_rotate(curr)
            return
        elif bf == 2:
            if get_height(curr.r.r) == get_height(curr.l) + 1:
                right_rotate(curr)
            else:
                left_rotate(curr.r)
                right_rotate(curr)
            return
        else:
            curr.height = max(get_height(curr.l), get_height(curr.r)) + 1
            curr = curr.parent
            
def AVL_insert(root, k):
    new_node = AVLNode(k)
    if root is None:
        return new_node
    new_node = BST_insert(root, k)
    fix_imbalance(new_node)
    return root
    
    
def right_rotate(root):
    """ perform a right rotate of the tree rooted at root
        and return the new root
    """
    node_r = root.r
    node_rl = node_r.l
    parent = root.parent
    
    root.r = node_rl
    if node_rl is not None:
        node_rl.parent = root
    
    node_r.l = root
    root.parent = node_r
    if parent is None:
        return node_r
    if parent.l is root:
        parent.l = node_r
    else:
        parent.r = node_r
    node_r.parent = parent
        
    root.height = max(get_height(root.l), get_height(root.r)) + 1
    node_r = max(get_height(node_r.l), get_height(node_r.r)) + 1
    return node_r
    

def left_rotate(root):
    """ perform a left rotate of the tree rooted at root
        and return the new root
    """
    node_l = root.l
    node_lr = node_l.r
    parent = root.parent
    
    root.l = node_lr
    if node_lr is not None:
        node_lr.parent = root
    
    node_l.r = root
    root.parent = node_l
    
    if parent is None:
        return node_l
    
    if parent.l is root:
        parent.l = node_l
    if parent.r is root:
        parent.r = node_l
    node_l.parent = parent
        
    root.height = max(get_height(root.l), get_height(root.r)) + 1
    node_l = max(get_height(node_l.l), get_height(node_l.r)) + 1
    return node_l
    
