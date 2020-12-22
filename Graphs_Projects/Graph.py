# Graph Class, Inherits Node Class
# Graph stores list of nodes and has implementation of different
# graph based algorithms like Djikstras

from Node import Node

class Graph(Node):
    # store nodes/edges as dictonary?
    def __init__(self,node_names,links):
        self.node_names = node_names
        self.edge_list = links
        self.node_list = dict(zip(self.node_names,[Node(node_name) for node_name in node_names]))
        self.node_list = self.node_list
        # Creating an empty dictionary to hold links
        self.graph = {node: [] for node in node_names}
        self.add_edge(self.edge_list)
        self.adjacency_matrix = []
        self.curr_num = 0
    
    def __str__(self):
        return "Hello"
    
    def get_node(self,node_name):
        return self.node_list.get(node_name)

    def add_node(self,node_name):
        self.node_list[node_name] = Node(node_name)

    def add_edge(self,links):
        # checks for single link added
        if type(links) == tuple:
            links = [links]
        # adds links to graph without duplications
        for node in self.node_names:
            for link in links:
                # checks for duplicate links
                if node == link[0] and link[1] not in self.graph[node]:
                    self.graph[node].append(link[1])
        
    def remove_edge(self,link):
        self.graph[link[0]].pop(self.graph[link[0]].index(link[1]))
    
    def eulerian_path(self):
       pass

    def connected_graph(self):
        pass

    def dijkstras(self):
        pass

    def MST(self):
        pass

if __name__ == "__main__":
    node_names = ["A","B","C"]
    node_links = [("A","B"),("A","C"),("A","C")]
    d = {i:[] for i in node_names}
    G = Graph(node_names,node_links)
    print(G.graph)
    node_links2 = ("B","C")
    G.add_edge(node_links2)
    print(G.graph)
    G.remove_edge(("A","C"))
    G.add_node("Z")
    print(G.graph)
    print(G.get_node("A"))
    for node in G.node_list:
        print(node)
    

    