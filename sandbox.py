# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Sandbox env

from graph import Graph
from mst import MST

# TODO:
#       - Create a class to make MST
#       - Implement MST algorithm
#       - Try running MST algo on test graph
#       - Attempt to construct the friend graph zach made
#       - Run MST on that

# TODO: Make the nodes csv and edge csv paths cmd line args

# Attempt to create graph object
g = Graph('./test_nodes.csv', './test_edges.csv')

print(g.nodes)
print(g.edges)

mst_maker = MST()

mst = mst_maker.compute_mst(g)

print("MST")
print(mst.nodes)
print(mst.edges)
