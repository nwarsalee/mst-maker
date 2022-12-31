# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Graph class

import csv
from node import Node, Nodes
from edge import Edge, Edges

class Graph:
    def __init__(self, nodes_path=None, edges_path=None, import_csv=True):
        self.nodes = Nodes()
        self.edges = Edges()

        if import_csv and nodes_path != None and edges_path != None:
            self.import_nodes_csv(nodes_path)
            self.import_edges_csv(edges_path)
        else:
            # TODO: Use a passed in string from user input
            pass
    

    def import_nodes_csv(self, path):
        with open(path) as file:
            lines = csv.reader(file)
            # parse each line of file into a singular node
            for row in lines:
                node = Node(row[0], row[1])
                self.nodes.add(node)


    def import_edges_csv(self, path):
        with open(path) as file:
            lines = csv.reader(file)
            # parse each line of file into a singular node
            for row in lines:
                # Find the nodes described in the entry
                src = self.nodes.find_by_id(row[0])
                dst = self.nodes.find_by_id(row[1])
                weight = row[2]

                # Create edge and add to collection of edges
                edge = Edge(src, dst, int(weight))
                self.edges.add(edge)
    
    def add_to_graph(self, edge):
        # Add onto graph based from an edge
        self.nodes.add(edge.src)
        self.nodes.add(edge.dst)

        self.edges.add(edge)

    def total_nodes(self):
        return self.nodes.total_nodes()
