import matplotlib.pyplot as plt
import networkx as nx

def plot_binary_tree(root):
    def add_nodes_edges(root, pos, x=0, y=0, x_step=0.2, level=0):
        if not root:
            return
        pos[root] = (x, -y)
        if root.left:
            G.add_edge(root, root.left)
            add_nodes_edges(root.left, pos, x - x_step/(2**level), y + 1, x_step, level+1)
        if root.right:
            G.add_edge(root, root.right)
            add_nodes_edges(root.right, pos, x + x_step/(2**level), y + 1, x_step, level+1)

    G = nx.DiGraph()
    pos = {}
    add_nodes_edges(root, pos)
    fig, ax = plt.subplots()

    nx.draw(G, pos, with_labels=False, arrows=False, 
      node_color='#4bc1dc', node_size=800, edge_color='gray', 
      linewidths=0.5, edgecolors='black'
    )
    labels = {node: node.val for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

    plt.show()