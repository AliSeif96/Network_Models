# Network_Models
Network Models with N=1000 and k=16



### 1. Random Graphs
- **Erdős–Rényi (ER) Graph**: A random graph where each pair of nodes is connected with a probability \( p \).
- **Chung-Lu Model**: Generates random graphs with a specified expected degree sequence.
- **Random k-Regular Graph**: Each node has exactly \( k \) neighbors, with edges assigned randomly.

### 2. Lattice-Based Networks
- **Regular Graph**: Each node is connected to a fixed number of nearest neighbors in a lattice structure.
- **Random Geometric Graph (RGG)**: Nodes are randomly placed in space, and edges form between nodes within a certain distance.
- **Small-World Network (Watts-Strogatz)**: Combines regular lattice with random rewiring to create small-world properties (high clustering, short path lengths).

### 3. Scale-Free Networks
- **Barabási-Albert (BA) Model**: Nodes are added to the network with preferential attachment, leading to a power-law degree distribution.
- **Holme-Kim Model**: A variant of the BA model that introduces clustering by adding triangles.

### 4. Community-Based Networks
- **Stochastic Block Model (SBM)**: Nodes are grouped into communities, with edges formed based on inter- and intra-community probabilities.

### 5. Geometric Networks
- **Random Geometric Graph (RGG)**: A 2D or 3D metric space defines the network topology, based on node proximity.
