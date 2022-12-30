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