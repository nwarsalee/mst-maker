# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# Node class

class Node:
    def __init__(self, name, type, descr="N/A"):
        self.name        = name
        self.type        = type
        self.description = descr
        self.label = name[:3].capitalize if len(name) > 3 else name
    
    def __str__(self):
        return "{} | {}".format(self.label, self.type)

class Nodes:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def get(self, index):
        return self.nodes[index]

    def total_nodes(self):
        return len(self.nodes)

    def find(self, id):
        for node in self.nodes:
            if node.name == id:
                return node
        
        return None

    def __str__(self):
        out = ""
        for node in self.nodes:
            out += str(node) + "\n"
        
        return out