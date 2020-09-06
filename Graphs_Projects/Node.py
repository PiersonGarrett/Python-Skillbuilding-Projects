class Node:
    def __init__(self,node_number):
        self.node_number = node_number
        self.edges = []
    
    def add_edge(self,connect_node,weight = 0):
        self.edges.append((self.node_number,connect_node,weight))
    
    def __str__(self):
        return str(self.edges)
