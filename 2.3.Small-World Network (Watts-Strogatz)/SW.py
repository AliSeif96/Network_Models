import networkx as nx
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Number of nodes
k = 16    # Each node connected to k closest neighbors
p = 0.1   # Rewiring probability (for small-world)

# Create the small-world network using the Watts-Strogatz model
G = nx.watts_strogatz_graph(n, k, p)

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.show()

# Print degree distribution
degrees = [G.degree(n) for n in G.nodes()]
print(f"Average degree: {sum(degrees) / len(degrees):.2f}")


import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_SW.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')