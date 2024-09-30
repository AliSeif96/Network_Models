import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters
n = 1000  # Total number of nodes
sizes = [277, 446, 277]  # Custom sizes for the three groups
k = 16  # Desired average degree

# Adjusted connection probabilities
p_intra = 0.042  # Probability of connection within a group (higher internal connectivity)
p_inter = 0.002  # Probability of connection between groups (lower inter-group connectivity)

# Define the connection probabilities matrix for 3 groups
# The diagonal values represent intra-group probabilities, and off-diagonal values represent inter-group probabilities
probs = [
    [p_intra, p_inter, p_inter],  # Group 1 connections
    [p_inter, p_intra, p_inter],  # Group 2 connections
    [p_inter, p_inter, p_intra]   # Group 3 connections
]

degrees=0
k_max=16.009
k_min=15.999

while (degrees>k_max or degrees<k_min):
    # Generate the Stochastic Block Model (SBM)
    G = nx.stochastic_block_model(sizes, probs)
    degrees = [G.degree(n) for n in G.nodes()]
    degrees = sum(degrees) / len(degrees)

# Plot the network
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)  # Spring layout for better separation

# Color nodes based on their group
node_colors = []
for i in range(n):
    if i < sizes[0]:
        node_colors.append("red")  # Group 1 (0 to 276)
    elif i < sizes[0] + sizes[1]:
        node_colors.append("blue")  # Group 2 (277 to 722)
    else:
        node_colors.append("green")  # Group 3 (723 to 999)

# Draw the network
nx.draw(G, pos, node_size=20, node_color=node_colors, with_labels=False, edge_color="gray", alpha=0.7)
plt.title("Hierarchical Network with 3 Groups (N=1000, k=16)")
plt.show()

# Calculate the actual average degree
degrees = [G.degree(n) for n in G.nodes()]
average_degree = np.mean(degrees)
print(f"Actual average degree: {average_degree:.2f}")


import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_BM0.042,0.002.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=300, with_labels=False, node_color=node_colors)
plt.savefig('pic0.042,0.002.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=300, with_labels=False, node_color=node_colors)
plt.savefig('pic_circular0.042,0.002.png')