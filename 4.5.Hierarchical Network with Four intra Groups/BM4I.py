import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters
n = 1000  # Total number of nodes
sizes = [250, 250, 250, 250]  # Four equal groups
k = 16  # Desired average degree


# Adjusted connection probabilities
#p_intra = 0.059  # Probability of connection within a group (higher internal connectivity)
#p_inter = 0.002  # Probability of connection between groups (lower inter-group connectivity)


x=0.0029

# Adjusted connection probabilities 0.05,0.01,0.002
p_intra_sub = x*16  # Probability of connection within a sub-group (higher internal connectivity) 0.06,0.004,0.0005
p_intra_main = x*4  # Probability of connection within a main group (less than sub-group)
p_inter = x  # Probability of connection between main groups (lower inter-group connectivity)




# Define the connection probabilities matrix for 4 groups0.059,0.002
# The diagonal values represent intra-group probabilities, and off-diagonal values represent inter-group probabilities
probs = [
    [p_intra_sub, p_intra_main, p_inter, p_inter],  # Group 1 connections
    [p_intra_main, p_intra_sub, p_inter, p_inter],  # Group 2 connections
    [p_inter, p_inter, p_intra_sub, p_intra_main],  # Group 3 connections
    [p_inter, p_inter, p_intra_main, p_intra_sub]   # Group 4 connections
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
pos = nx.spring_layout(G)  # Spring layout for better separation

# Color nodes based on their group
node_colors = []
for i in range(n):
    if i < sizes[0]:
        node_colors.append("red")  # Group 1
    elif i < sizes[0] + sizes[1]:
        node_colors.append("blue")  # Group 2
    elif i < sizes[0] + sizes[1] + sizes[2]:
        node_colors.append("green")  # Group 3
    else:
        node_colors.append("purple")  # Group 4

# Draw the network
nx.draw(G, pos, node_size=20, node_color=node_colors, with_labels=False, edge_color="gray", alpha=0.7)
plt.title("Hierarchical Network with 4 Groups (N=1000, k=16)")
plt.show()

# Calculate the actual average degree
degrees = [G.degree(n) for n in G.nodes()]
average_degree = np.mean(degrees)
print(f"Actual average degree: {average_degree:.2f}")


import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge) 0.0464,0.0116,0.0029
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_BM0.0464,0.0116,0.0029.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=300, with_labels=False, node_color=node_colors)
plt.savefig('pic0.0464,0.0116,0.0029.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=300, with_labels=False, node_color=node_colors)
plt.savefig('pic_circular0.0464,0.0116,0.0029.png')