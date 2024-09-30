import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Number of nodes
expected_degrees = np.full(n, 16)  # Expected degree for each node



degrees=0
k_max=16.009
k_min=15.999

while (degrees>k_max or degrees<k_min):
    # Create the Chung-Lu graph
    G = nx.expected_degree_graph(expected_degrees, selfloops=False)
    degrees = [G.degree(n) for n in G.nodes()]
    degrees = sum(degrees) / len(degrees)



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
np.savetxt('Matrix_ED.txt',adj_matrix, delimiter='\t',fmt='%i')



# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')

# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')