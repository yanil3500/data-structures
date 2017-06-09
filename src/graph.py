
class Graph():
    """
    The graph class will be used o represent the nodes
    """
    def __init__(self):
        """
        This is the initializer for the Graph class.
        """
        self.graph_dict = {}
        self.size = 0

    def nodes(self):
        """
        This method returns a list containing all of the nodes
        """
        return list(self.graph_dict.keys())

    def edges(self):
        """
        This method returns a list containing all of the edges
        """
        a_list = []
        for key in self.graph_dict.keys():
            if self.graph_dict[key]:
                a_list.append((key, self.graph_dict[key]))
        return a_list

    def add_node(self, val):
        """
        This method adds a node to our graph
        """
        if val not in self.graph_dict:
            self.size += 1
            self.graph_dict[val] = {}

    def add_edge(self, val1, val2, weight=1):
        """
        this method adds a new edge to the graph connecting
        the node containing 'val1' and 'val2'
        """
        self.add_node(val1)
        self.add_node(val2)
        self.graph_dict[val1][val2] = weight

    def del_node(self, val):
        if val not in self.graph_dict:
            raise KeyError('The (key) node is not in the graph.')
        for key in self.graph_dict[val]:
            if val in self.graph_dict[key]:
                self.graph_dict[key].remove(val)
                self.size -= 1
        del self.graph_dict[val]

    def del_edge(self, val1, val2):
        """
        This method will delete the edge between the given values, val1 and val2, if such edge exists.
        If the connection between val1 and val2 does not exist, then this method will raise an exception
        indicating as much.
        """
        if val2 not in self.graph_dict[val1]:
            raise ValueError("The edge does not exists.")
        else:
            self.graph_dict[val1].pop(val2, None)

    def has_node(self, val):
        """
        This method checks if the given value is an element in the graph.
        """
        return val in self.graph_dict

    def neighbors(self, val):
        """
        This method checks if the given value has any neighbors. Returns list of neighbors if true
        """
        if val not in self.graph_dict:
            raise KeyError("The node not present in the graph.")
        return self.graph_dict[val]

    def adjacent(self, val1, val2):
        """
        This method returns True if there is edge an connecting the given values, else it returns False; Raises an exception if either of the
        given values are not present in the graph.
        """
        if val1 not in self.graph_dict or val2 not in self.graph_dict:
            raise KeyError("The nodes are not present in the graph.")
        return val2 in self.graph_dict[val1]



def main():
    """
    main function
    """
    a_graph = Graph()
    a_graph.add_node('B')
    a_graph.add_node('A')
    a_graph.graph_dict['B']['C'] = 1
    a_graph.add_edge('A', 'B', 100)
    a_graph.add_edge('A', 'C', 3)
    a_graph.add_edge('B', 'D', 50)
    a_graph.add_edge('C', 'D', 5)
    # a_graph.del_edge('B', 'D')
    a_graph.del_node('A')
    # print(a_graph.neighbors('B'))
    # print(a_graph.adjacent('A', 'B'))

if __name__ == "__main__":
    main()