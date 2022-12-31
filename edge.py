# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Edge class

from operator import attrgetter

class Edge:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
    
    def contains(self, node):
        return self.src == node or self.dst == node

    def __str__(self):
        return "[{}, {}] - {}u".format(self.src.label, self.dst.label, self.weight)
    
    def __rpr__(self):
        return "[{}, {}] - {}u".format(self.src.label, self.dst.label, self.weight)
    
    def __eq__(self, other):
        return self.src == other.src and self.dst == other.dst


class Edges:
    def __init__(self):
        self.edges = []

    def add(self, edge):
        # Don't add the edge if it's a duplicate
        if self.find_by_edge(edge):
            return

        self.edges.append(edge)
    
    def extend(self, edge_list):
        for edge in edge_list:
            self.add(edge)

    def get(self, index):
        return self.edges[index]
    
    def get_all(self):
        return self.sort_edges(self.edges)

    def total_edges(self):
        return len(self.edges)

    def find(self, src, dst):
        for edge in self.edges:
            if edge.src == src and edge.dst == dst:
                return edge
        
        return False

    def find_by_edge(self, src_edge):
        for edge in self.edges:
            if edge == src_edge:
                return edge
        
        return False
    
    # Function to find all edges containing a given node
    def find_all(self, node):
        edges = []
        for edge in self.edges:
            if edge.contains(node):
                edges.append(edge)

        return self.sort_edges(edges)

    def pop(self):
        # Removes the lowest weighted edge
        
        # Sort edges
        self.edges = self.sort_edges(self.edges)

        # Remove first
        return self.edges.pop(0)

    
    def __str__(self):
        out = ""
        for edge in self.edges:
            out += str(edge) + "\n"
        
        return out
    
    def sort_edges(self, edges):
        return sorted(edges, key=lambda x: x.weight)

    def min_edge(self):
        return min(self.edges, key=lambda x: x.weight)

    def total_weight(self):
        return sum(e.weight for e in self.edges)