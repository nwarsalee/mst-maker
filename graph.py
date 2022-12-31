# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Graph class

import csv
from node import Node, Nodes
from edge import Edge, Edges

class Graph:
    def __init__(self, nodes_path, edges_path, import_csv=True):
        self.nodes = Nodes()
        self.edges = Edges()

        if import_csv:
            # TODO: Perform functions that will read in CSV file and create nodes
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
                src = self.nodes.find(row[0])
                dst = self.nodes.find(row[1])
                weight = row[2]

                # Create edge and add to collection of edges
                edge = Edge(src, dst, int(weight))
                self.edges.add(edge)
        
        print(self.edges)
