# Graph Class, Inherits Node Class
# Graph stores list of nodes and has implementation of different
# Graph based algorithsm like Djikstras

import Node

class Graph:
    def __init__(self):
       self.node_list = []
    
    def get_node(self,node_number):
        return self.node_list[node_number]

    def eulerian_path(self):
        pass

    def connected_graph(self):
        pass

    def dijkstras(self):
        pass

    def MST(self):
        pass


    


