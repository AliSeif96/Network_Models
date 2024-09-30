import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 1000  # Total number of nodes
sizes = [500, 500]  # Two equal-sized communities
p_intra = 0.0285     # Probability of connection within a block (adjust for degree 16)
p_inter = 0.004     # Probability of connection between blocks

# Create the stochastic block model
probs = [[p_intra, p_inter], [p_inter, p_intra]]

degrees=0
k_max=16.009
k_min=15.999

while (degrees>k_max or degrees<k_min):
    # Create the random geometric graph
    G = nx.stochastic_block_model(sizes, probs)
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
np.savetxt('Matrix_SBM.txt',adj_matrix, delimiter='\t',fmt='%i')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=10, with_labels=False)
plt.savefig('pic.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=10, with_labels=False)
plt.savefig('pic_circular.png')



import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters
n = 1000  # Total number of nodes
n_group = n // 2  # Size of each group (500)
k = 16  # Desired average degree
p_intra = 0.0305     # Probability of connection within a block (adjust for degree 16)
p_inter = 0.002     # Probability of connection between blocks

# Define the sizes of the two groups0.0305,0.002
sizes = [n_group, n_group]

# Define the connection probabilities matrix
probs = [[p_intra, p_inter], 
         [p_inter, p_intra]]


degrees=0
k_max=16.009
k_min=15.999

while (degrees>k_max or degrees<k_min):
    #Generate the Stochastic Block Model (SBM)
    G = nx.stochastic_block_model(sizes, probs)
    degrees = [G.degree(n) for n in G.nodes()]
    degrees = sum(degrees) / len(degrees)




# Plot the network
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)  # Spring layout for better separation
nx.draw(G, pos, node_size=20, node_color=["red" if n < n_group else "blue" for n in G.nodes()])
plt.show()

# Calculate the actual average degree
degrees = [G.degree(n) for n in G.nodes()]
average_degree = np.mean(degrees)
print(f"Actual average degree: {average_degree:.2f}")



import numpy as np

# Convert to a binary adjacency matrix (1 for edge, 0 for no edge)
adj_matrix = nx.to_numpy_array(G, dtype=int)
np.savetxt('Matrix_SBM0.0305,0.002.txt',adj_matrix, delimiter='\t',fmt='%i')



# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw(G, node_size=20, with_labels=False, node_color=["red" if n < n_group else "blue" for n in G.nodes()])
plt.savefig('pic0.0305,0.002.png')


# Draw the graph
plt.figure(figsize=(80, 80))
nx.draw_circular(G, node_size=20, with_labels=False, node_color=["red" if n < n_group else "blue" for n in G.nodes()])
plt.savefig('pic_circular0.0305,0.002.png')