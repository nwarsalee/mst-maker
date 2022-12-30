# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Sandbox env

from node import Node
from edge import Edge

# Create list of nodes
names = ["A", "B", "C", "D"]

nodes = []
edges = []

for name in names:
    temp = Node(name, 0)
    nodes.append(temp)

# Create manual node connections
e1 = Edge(nodes[0], nodes[1], 5)
e2 = Edge(nodes[0], nodes[2], 3)
e3 = Edge(nodes[3], nodes[1], 4)
e4 = Edge(nodes[3], nodes[2], 1)

edges.append(e1)
edges.append(e2)
edges.append(e3)
edges.append(e4)

# Print out nodes
for node in nodes:
    print(node)

# Print out nodes
for edge in edges:
    print(edge)

