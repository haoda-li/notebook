# we will use python-igraph as 
# our graph implementation to simplify life
from math import inf
import igraph as ig
import matplotlib.pyplot as plt
from matplotlib.cm import Reds_r as palette
PLOT_SETTINGS = dict(vertex_size=10, vertex_label_dist=10, vertex_label_size=14)
UNDISCOVERED, DISCOVERED, FINISHED = 0, 1, 2

# We will use python's list to implement a queue
# although this is wasteful, but good for illustration
class Queue:
    def __init__(self) -> None:
        self.q = []
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.pop(0)
    def empty(self):
        return len(self.q) == 0
    
def traversal_order(traversal_alg, G, s):
    G.vs['order'] = inf
    order = 0
    def fn_order(v): 
        nonlocal order
        G.vs[v]['order'] = order
        order += 1
    traversal_alg(G, s, fn_order)
    
def plot_graph(g, labels, layout, path):
    fig, axs = plt.subplots(1, 2, figsize=(16, 6));
    for i, label in enumerate(labels):
        axs[i].set_axis_off(); axs[i].set_title(label)
        max_label = max(set(g.vs[label]) - {inf}) + 1
        colors = palette([(x + 1)/ max_label for x in g.vs[label]])
        colors = [list(x) for x in colors]
        ig.plot(g, target=axs[i], 
                vertex_label=g.vs[label],
                vertex_color=colors, 
                layout = layout,
                **PLOT_SETTINGS)
    fig.savefig(path)
    
def BFS(G, s, fn):
    """ Given the graph and index
        perform fn on traversed node
        with breadth first search order
    """
    G.vs['distance'] = inf
    q = Queue()
    G.vs['state'] = UNDISCOVERED
    q.enqueue(s)
    G.vs[s]['distance'] = 0
    G.vs[s]['state'] = DISCOVERED
    while not q.empty():
        v = q.dequeue()
        fn(v)
        G.vs[v]['state'] = FINISHED
        distance = G.vs[v]['distance']
        for u in G.neighbors(v):
            if G.vs[u]['state'] == UNDISCOVERED:
                q.enqueue(u)
                G.vs[u]['state'] = DISCOVERED
                G.vs[u]['distance'] = distance + 1
    

def DFS(G, s, fn):
    """ Given the graph and index
        perform fn on traversed node
        with breadth depth search order
    """
    G.vs['state'] = UNDISCOVERED
    G.vs['d'] = inf
    G.vs['f'] = inf
    time = 0
    def visit(G, u):
        nonlocal time
        time += 1
        G.vs[u]['d'] = time
        G.vs[u]['state'] = DISCOVERED
        for v in G.neighbors(u):
            if G.vs[v]['state'] == UNDISCOVERED:
                visit(G, v)
        G.vs[u]['state'] = FINISHED
        fn(u)
        time += 1
        G.vs[u]['f'] = time
    visit(G, s)
    
    
def topological_sort(G):
    G.vs['state'] = UNDISCOVERED
    G.vs['order'] = inf
    G.vs['f'] = inf
    time = 0
    order = 0
    def visit(G, u):
        nonlocal time
        nonlocal order
        time += 1
        G.vs[u]['d'] = time
        G.vs[u]['state'] = DISCOVERED
        for v in G.neighbors(u, mode="in"):
            if G.vs[v]['state'] == UNDISCOVERED:
                visit(G, v)
        G.vs[u]['state'] = FINISHED
        order += 1
        G.vs[u]['order'] = order
        time += 1
        G.vs[u]['f'] = time
    for i in range(len(G.vs)):
        if G.vs[i]['state'] == UNDISCOVERED:
            visit(G, i)