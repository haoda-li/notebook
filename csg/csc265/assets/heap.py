from .priority_queue import PriorityQueue
    
class Heap(PriorityQueue):
    def __init__(self, arr, ascending=False):
        self.H = arr
        if ascending:
            self.compare = lambda x, y: x < y
        else:
            self.compare = lambda x, y: x > y
        for i in range(len(arr) // 2, -1, -1):
            self.__heapify(i)
            
        
    @staticmethod
    def left(i):
        "given the index, return the index of left child"
        return 2 * i + 1
    
    @staticmethod
    def right(i):
        "given the index, return the index of right child"
        return 2 * i + 2
    
    @staticmethod
    def parent(i):
        "given the index, return the index of parent"
        return (i - 1)// 2
    
    def __heapify(self, i):
        """ Given the complete binary tree H and index i, 
            assume that the left subtree and right subtree of 
            of H[i] are max-heap.
            make H a max heap
        """
        largest = i
        l, r = Heap.left(i), Heap.right(i)
        if l < len(self.H) and self.compare(self.H[l], self.H[largest]):
            largest = l
        if r < len(self.H) and self.compare(self.H[r], self.H[largest]):
            largest = r
        if largest != i:
            self.H[i], self.H[largest] = self.H[largest], self.H[i]
            self.__heapify(largest)
            
    def peek(self):
        return self.H[0]
    
    def pull(self):
        m = self.H[0]
        self.H[0] = self.H[-1]
        self.H.pop()
        self.__heapify(0)
        return m
    
    def insert(self, x):
        self.H.append(x)
        i = len(self.H) - 1
        while self.compare(self.H[i], self.H[Heap.parent(i)]) and i != 0:
            self.H[i], self.H[Heap.parent(i)] = self.H[Heap.parent(i)], self.H[i]
            i = Heap.parent(i)
            
    def plot(self, path):
        from .plot_trees import TreeNode, plot_tree
        if len(self.H) == 0:
            return
        nodes = [TreeNode(str(self.H[0]))]
        for i in range(1, len(self.H)):
            new_node = TreeNode(str(self.H[i]), nodes[Heap.parent(i)])
            nodes.append(new_node)
            nodes[Heap.parent(i)].children.append(new_node)

        return plot_tree(nodes[0], path)
            
def heap_sort(arr, ascending=False):
    H = Heap(arr, ascending=ascending)
    sorted = []
    for _ in range(len(arr)):
        sorted.append(H.pull())
    return sorted

