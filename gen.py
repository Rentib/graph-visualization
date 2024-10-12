import matplotlib.pyplot as plt
import networkx as nx
import os

os.makedirs("figures", exist_ok=True)

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",  # Use pdflatex for processing
    "font.family": "serif",       # Use serif font (matches LaTeX default)
    "text.usetex": True,          # Use LaTeX for text rendering
})

G = nx.Graph()
G.add_edges_from([
    (1, 2), (1, 3), (2, 4), (2, 5), (2, 6),
    (3, 5), (3, 6), (4, 7), (4, 8), (5, 7),
    (5, 8), (6, 7), (6, 8), (7, 9), (8, 9)
])
pos = nx.bfs_layout(G, 1)

nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='white',
        edgecolors='black',
        node_size=1000,
        edge_color='black')

plt.savefig("./figures/fig1.pgf", format="pgf")
