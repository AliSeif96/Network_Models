import networkx as nx
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Number of nodes
m = 8     # Number of edges to attach from a new node to existing nodes
p = 0.1   # Probability of adding a triangle (to increase clustering)

# Create the scale-free network using the Holme-Kim model
G = nx.powerlaw_cluster_graph(n, m, p)

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw(G, node_size=10, with_labels=False)
plt.show()

# Print the actual average degree of the generated network
degrees = [G.degree(n) for n in G.nodes()]
print(f"Actual average degree: {sum(degrees) / len(degrees):.2f}")


import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_HK.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')