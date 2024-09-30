import networkx as nx
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Number of nodes
k = 16    # Desired degree for each node

# Create the random regular graph
G = nx.random_regular_graph(k, n)

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw(G, node_size=10, with_labels=False)
plt.show()

# Print the actual average degree
degrees = [G.degree(n) for n in G.nodes()]
print(f"Actual average degree: {sum(degrees) / len(degrees):.2f}")

import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_KRR.txt',adj_matrix, delimiter='\t',fmt='%i')

# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')