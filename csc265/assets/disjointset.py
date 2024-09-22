from .plot_trees import plot_tree, construct_tree_nodes

class DNode:
    def __init__(self, x) -> None:
        self.value = x
        self.rank = 0
        self.parent = self
        # this is only for easy printing
        self.children = []
        
class DisjointSet:
    
    def __init__(self) -> None:
        self.nodes = []
        self.n = 0
        
        
    def makeset(self, x):
        self.nodes.append(DNode(x))
        self.n += 1
        
    # path compression
    def findset(self, node):
        if node.parent is node:
            return node
        root = self.findset(node.parent)
        if node.parent is not root:
            root.children.append(node)
            node.parent.children.remove(node)
            node.parent = root
        return root
    
    def findset_naive(self, node):
        if node.parent is node:
            return node
        return self.findset_naive(node.parent)
    
    def union(self, x, y):
        sx = self.findset(x)
        sy = self.findset(y)
        if sx is not sy:
            self.__link(sx, sy)
            self.n -= 1
            
    def union_naive(self, x, y):
        sx = self.findset_naive(x)
        sy = self.findset_naive(y)
        if sx is not sy:
            self.__link_naive(sx, sy)
            self.n -= 1
            
    def union_weighted(self, x, y):
        sx = self.findset_naive(x)
        sy = self.findset_naive(y)
        if sx is not sy:
            self.__link(sx, sy)
            self.n -= 1
            
    def union_compression(self, x, y):
        sx = self.findset(x)
        sy = self.findset(y)
        if sx is not sy:
            self.__link_naive(sx, sy)
            self.n -= 1

    # weighted union
    def __link(self, x, y):
        if x.rank > y.rank:
            y.parent = x
            x.children.append(y)
        elif x.rank < y.rank:
            x.parent = y
            y.children.append(x)
        else:
            y.parent = x
            x.children.append(y)
            x.rank += 1
            
    def __link_naive(self, sx, sy):
        sx.parent = sy
        sy.children.append(sx)
        sy.rank = max(sy.rank, sx.rank + 1)
        
            
    def plot(self, label_fn, path):
        counter, i = 0, 0
        root = DNode(r"$\mathcal S$")
        while counter < self.n:
            node = self.nodes[i]
            if node.parent is node:
                root.children.append(node)
                counter += 1
            i += 1
        return plot_tree(construct_tree_nodes(root, label_fn, children_attr="children"), path)
        
                
            
    