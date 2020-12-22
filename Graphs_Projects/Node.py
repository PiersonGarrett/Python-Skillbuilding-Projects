class Node:
    def __init__(self,name):
        self.node_name = name
        self.visited = 0
        #self.edges = []
    
    
    def __str__(self):
        return f"Node Name: {self.node_name}, Visited {self.visited}"
