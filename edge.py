# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Edge class

import node

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
    
    def __str__(self):
        return "[{}, {}] - {}u".format(self.src.label, self.dst.label, self.weight)


class Edges:
    def __init__(self):
        self.edges = []

    def add(self, edge):
        self.edges.append(edge)

    def get(self, index):
        return self.edges[index]

    def total_edges(self):
        return len(self.edges)

    def find(self, src, dst):
        for edge in self.edges:
            if edge.src == src and edge.dst == dst:
                return edge
        
        return None