import networkx as nx
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Number of nodes
k = 16    # Each node connected to k closest neighbors
p = 0     # Rewiring probability (0 for regular network)

# Create the regular network using the Watts-Strogatz model with p=0
G = nx.watts_strogatz_graph(n, k, p)

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.show()

# You can also access neighbors for any node. For example:
node = 220
print(f"Neighbors of node {node}: {list(G.neighbors(node))}")

node = 999
print(f"Neighbors of node {node}: {list(G.neighbors(node))}")


import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_RG.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')

# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')