
import plotly.graph_objects as go
import plotly

class TreeNode:
    def __init__(self, label, parent=None) -> None:
        self.label = label
        self.children = []
        self.level = 0 if parent is None else parent.level + 1
        self.width = 1
        
def update_width(node):
    if len(node.children) == 0:
        node.width = 1
    else:
        node.width = sum([update_width(child) for child in node.children])
    return node.width
        

def construct_tree_nodes(root, label_fn=None, child_attrs=[], children_attr=None):
    def rec(node, parent):
        if node is None:
            return None
        text = label_fn(node)
        pnode = TreeNode(text, parent)
        if parent is not None:
            parent.children.append(pnode)
        for attr in child_attrs:
            rec(getattr(node, attr), pnode)
        if children_attr is not None:
            for child in getattr(node, children_attr):
                rec(child, pnode)
        return pnode
    return rec(root, None)

def graph_to_plot(root):
    x, y, label, ex, ey = [], [], [], [], []

    def rec(node, start, parent_x, parent_y):
        curr_x = start + node.width / 2
        curr_y = node.level * -1
        x.append(curr_x)
        y.append(curr_y)
        label.append(node.label)
        if parent_y < 1:
            ex.append(parent_x)
            ex.append(curr_x)
            ex.append(None)
            ey.append(parent_y)
            ey.append(curr_y)
            ey.append(None)
        child_start = start
        for child in node.children:
            rec(child, child_start, curr_x, curr_y)
            child_start += child.width
    rec(root, 0, 1, 1)
    
    
    return x, y, label, ex, ey

def plot_tree(root, path):
    update_width(root)
    vx, vy, labels, edge_x, edge_y = graph_to_plot(root)
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    vertex_trace = go.Scatter(
        x=vx, y=vy,
        text=labels,
        mode="text"
    )

    fig = go.Figure([edge_trace, vertex_trace])

    axis = dict(
        showline=False, 
        zeroline=False,
        # showgrid=False,
        showticklabels=False,
    )

    fig.update_layout(
        width=720,
        height=min(vy) * -80,
        font_size=14,
        showlegend=False,
        xaxis=axis,
        yaxis=axis,
        margin=dict(l=0, r=0, b=5, t=2),
        plot_bgcolor='rgb(255,255,255)'
    )
    return plotly.io.write_image(fig, path)

    