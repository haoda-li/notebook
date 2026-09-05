import igraph as ig
import matplotlib.pyplot as plt
PLOT_SETTINGS = dict(
    vertex_color="white", 
    vertex_label_size=14, edge_color="gray", autocurve=True, margin=(0,0,0,0)
)

E = []
for i in range(1, 6):
    for j in range(i):
        E.append((j,i))
g = ig.Graph(n=6, edges=E, directed=True)
fig, ax = plt.subplots(figsize=(4, 4)); ax.set_axis_off(); ax.set_title("N=6, full model")
ig.plot(g, target=ax, vertex_label=[1,2,3,4,5,6], layout=g.layout(), **PLOT_SETTINGS)
fig.tight_layout()
fig.savefig("../assets/dag_1.jpg")


g = ig.Graph(n=6, edges=[(0, 1), (0, 2), (2, 4), (4, 5), (1, 5), (1, 3)], directed=True)
fig, ax = plt.subplots(figsize=(4, 4)); ax.set_axis_off();
ig.plot(g, target=ax, vertex_label=[1,2,3,4,5,6], 
        layout=g.layout("rt"), **PLOT_SETTINGS)
fig.tight_layout()
fig.savefig("../assets/dag_2.jpg")


cases = ["Chain", "Common Cause", "Explaning Away"]
edge_sets = [[(0, 1), (1, 2)], [(1, 0), (1, 2)], [(2, 1), (0, 1)]]
fig, axs = plt.subplots(1, 3, figsize=(12, 4)); 
for i, (case, edges) in enumerate(zip(cases, edge_sets)):
    g = ig.Graph(n=3, edges=edges, directed=True)
    axs[i].set_axis_off(); axs[i].set_title(case)
    ig.plot(g, target=axs[i], vertex_label=["X", "Y", "Z"], 
            layout=g.layout("rt"), **PLOT_SETTINGS)
fig.tight_layout()
fig.savefig("../assets/dag_3.jpg")  