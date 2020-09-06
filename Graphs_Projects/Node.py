class Node:
    def __init__(self,num=0):
        self.node_number = num
        self.visited = 0
        #self.edges = []
    
    
    def __str__(self):
        return f"Node Number: {self.node_number}, Visited {self.visited}"
