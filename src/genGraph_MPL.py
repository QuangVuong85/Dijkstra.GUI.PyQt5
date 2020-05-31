import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


G = nx.Graph()  # Create empty graph

G.add_nodes_from(["A", "B", "C"])  # Add nodes

# Add edges
G.add_edge("A", "B", weight=5)
G.add_edge("B", "C", weight=7)
G.add_edge("C", "A", weight=2)

# Create drawing
pos = nx.spring_layout(G)  # List of positions of nodes
weights = nx.get_edge_attributes(G, "weight") # List of weights
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

plt.title("Basic Graphs with Networkx")
plt.gcf().canvas.set_window_title("")  # Hide window title

# Display Graph
plt.show()