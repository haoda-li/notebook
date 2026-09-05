from math import inf

from matplotlib.pyplot import plot
from .priority_queue import PriorityQueue
from .plot_trees import TreeNode, construct_tree_nodes, plot_tree

class Node:
    def __init__(self, k):
        self.k = k
        self.children = []
    
    @property
    def degree(self):
        return len(self.children)
    
    def add(self, other):
        if self.degree != other.degree:
            raise ValueError("Cannot merge binomial trees of different size")
        self.children.insert(0, other)
        
        
class MergableHeap(PriorityQueue):
    def __init__(self, arr=[], ascending=False):
        self.trees = dict()
        self.bit = -1
        self.ascending = ascending
        if ascending:
            self.compare = lambda x, y: x < y
        else:
            self.compare = lambda x, y: x > y
        for x in arr:
            self.insert(x)
        
    def from_trees(self, trees):
        for tree in trees:
            self.trees[tree.degree] = tree
            if tree.degree > self.bit:
                self.bit = tree.degree

    def __peek_node(self):
        m, trees_k = inf, -1
        for i, node in self.trees.items():
            if self.compare(node.k, m):
                m = node.k
                trees_k = i
        return self.trees[trees_k]
    
    def peek(self):
        return self.__peek_node().k
    
    def union(self, other):
        if self.ascending != other.ascending:
            raise ValueError("Two Mergable Heaps have different order")
        if other.bit == -1:
            return
        if self.bit == -1:
            self.trees = other.trees
            self.bit = other.bit
            return
        bit, max_bit = 0, max(self.bit, other.bit)
        new_trees = dict()
        reg = []
        while bit <= max_bit:
            if self.trees.get(bit):
                reg.append(self.trees[bit])
            if other.trees.get(bit):
                reg.append(other.trees[bit])
            if len(reg) == 1:
                new_trees[bit] = reg.pop()
            elif len(reg) == 2:
                t1 = reg.pop()
                t2 = reg.pop()
                if self.compare(t1.k, t2.k):
                    t1.add(t2)
                    reg.append(t1)
                else:
                    t2.add(t1)
                    reg.append(t2)
            elif len(reg) == 3:
                new_trees[bit] =  reg.pop()
                t1 = reg.pop()
                t2 = reg.pop()
                if self.compare(t1.k, t2.k):
                    t1.add(t2)
                    reg.append(t1)
                else:
                    t2.add(t1)
                    reg.append(t2)
            bit += 1
        if len(reg) == 1:
            new_trees[bit] = reg.pop()
        else:
            bit -= 1
        self.trees = new_trees
        self.bit = bit
        
    def insert(self, k):
        if len(self.trees) == 0:
            self.trees[0] = Node(k)
            self.bit = 0
        else:
            new_mh = MergableHeap([k], ascending=self.ascending)
            self.union(new_mh)
        
        
    def pull(self):
        m = self.__peek_node()
        del self.trees[m.degree]
        other = MergableHeap(ascending=self.ascending)
        other.from_trees(m.children)
        self.union(other)
        return m.k
    
    def plot(self, path):
        forest_root = TreeNode("")
        for tree in self.trees.values():
            forest_root.children.append(construct_tree_nodes(tree, label_fn=lambda x: x.k, children_attr ="children"))
        return plot_tree(forest_root, path)
    
