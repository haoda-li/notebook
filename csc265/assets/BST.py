class BSTNode:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.k = key
        self.l = None
        self.r = None
        
def insert(node, k):
 
    # If the tree is empty, return a new node
    if node is None:
        return BSTNode(k)
 
    # Otherwise recur down the tree
    if k < node.k:
        node.l = insert(node.l, k)
    else:
        node.r = insert(node.r, k)
 
    # return the (unchanged) node pointer
    return node


def search(node, k):
    if node is None:
        return False
    if node.k == k:
        return True
    if k < node.k:
        return search(node.l, k)
    else:
        return search(node.r, k)
    
def delete(node, k):
    if node is None:
        return node
    if k < node.k:
        node.l = delete(node.l, k)
    elif k > node.k:
        node.r = delete(node.r, k)
    elif node.l is None:
        temp = node.r
        node = None
        return temp
    elif node.r is None:
        temp = node.l
        node = None
        return temp
    else:
        temp = node.r
        while temp.l is not None:
            temp = temp.l
        node.k = temp.k
        node.r = delete(node.r, temp.k)
    return node