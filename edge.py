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