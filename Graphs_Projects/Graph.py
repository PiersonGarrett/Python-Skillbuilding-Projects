# Graph Class, Inherits Node Class
# Graph stores list of nodes and has implementation of different
# Graph based algorithsm like Djikstras

from Node import Node

class Graph(Node):
    
    def __init__(self):
        self.node_list = []
        self.edge_list = []
        self.adjacency_matrix = []
        self.curr_num = 0
    
    def __str__(self):
        return str(self.node_list[:])
    
    def add_edge(self,node1,node2,weight = 0):
        if (node1.node_number, node2.node_number,weight) not in self.edge_list:
            self.edge_list.append((node1.node_number, node2.node_number,weight))
    
    def get_node(self,node_number):
        return self.node_list[node_number]
    
    def create_node(self):
        new_node = Node(self.curr_num)
        self.node_list.append(new_node)
        self.curr_num += 1
    
    # for an undirected graph use method with directed = 0, for directed set directed = 1
    def generate_adjacency_matrix(self,directed = 0):
        # need to use this expression to generate matrix otherwise columns become linked
        self.adjacency_matrix = [[0]*len(self.node_list) for i in range(len(self.node_list))]
        
        if directed == 1:
            for edge in self.edge_list:
                self.adjacency_matrix[edge[0]][edge[1]] = 1
        elif directed == 0:
            for edge in self.edge_list:
                self.adjacency_matrix[edge[0]][edge[1]] = 1
                self.adjacency_matrix[edge[1]][edge[0]] = 1
        
        print(self.adjacency_matrix)
    
    def eulerian_path(self):
        path = []
        


    def connected_graph(self):
        pass

    def dijkstras(self):
        pass

    def MST(self):
        pass


    


if __name__ == "__main__":
    G = Graph()
    G.create_node()
    G.create_node()
    G.create_node()
    G.add_edge(G.node_list[0],G.node_list[1])
    G.add_edge(G.node_list[0],G.node_list[2])
    
    G.generate_adjacency_matrix(1)
    