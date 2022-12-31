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
                print(row)


    def import_edges_csv(self, path):
        # NOTE: Need to use nodes within nodes list (maybe need a find function)
        pass
