# All code below is from the NetworkX tutorials at https://networkx.org/documentation/stable/tutorial.html

import networkx as nx

class NetworkXTutorial:
    """This class works through the NetworkX Tutorial on the website listed above.

    Attributes
    ----------
    G : Graph
        a NetworkX graph object

    Methods
    -------
    using_nodes()
        Adds and removes nodes from a graph
    using_edges()
        Adds and removes edges from a graph
    directed_graphs()
        Creates a directed graph
    num_nodes()
        Returns the number of nodes in a graph
    num_edges()
        Returns the number of edges in a graph
    view_graph()
        Returns the nodes and edges in a graph
    construct_graph()
        Returns a directed graph constructed from another graph
    construct_from_edges(newGraph)
        Returns a graph constructed from the edges of the directed graph from construct_graph()
    construct_from_adj_dict()
        Returns a graph constructed from an adjacency dictionary
    access_graph()
        Allows quick access to all nodes and edges in a graph
    """
    def __init__(self, G):
        # Create an empty graph with no nodes and no edges
        self.G = G

    def using_nodes(self, G):
        """This function creates a graph and then adds and removes nodes.
        Returns
        -------
        Graph
            a nx Graph with only nodes 
        """
        self.G = nx.Graph()
        # Add a node one at a time
        self.G.add_node(1)
        # Add nodes from an iterable container (e.g. a list)
        self.G.add_nodes_from([2,3])
        # Add nodes along with node attributes of the form (node, node_attribute_dict)
        self.G.add_nodes_from([
            (4, {"color": "red"}),
            (5, {"color": "green"})
        ])
        # Nodes from one graph can be incorporated into another
        H = nx.path_graph(10)
        self.G.add_nodes_from(H) # H could also be used as a node in G itself
        self.G.add_node("node") # adds node "node"
        self.G.add_nodes_from("node") # adds 4 nodes: 'n', 'o', 'd', 'e'
        # Remove node from a graph
        self.G.remove_node(2)
        self.G.remove_nodes_from("node")
        return self.G

    def using_edges(self, G):
        """This function adds and removes edges from a graph.
        
        Returns
        -------
        Graph
            a nx Graph with nodes and edges 
        """
        # Add an edge at a time
        self.G.add_edge(1,2)
        edge = (2,3)
        self.G.add_edge(*edge) # unpack edge tuple*
        # Add edges from a list
        self.G.add_edges_from([(1, 2),(1,3)])
        # Add any ebunch (any iterable container of edge-tuples) of edges 
        H = nx.path_graph(10)
        self.G.add_edges_from(H.edges)
        # NetworkX ignores any already present nodes/edges
        self.G.add_edges_from([(1,2), (3,4)])
        self.G.add_edge(1,2)
        self.G.add_edge(3, 'm')
        # Remove edge from a graph
        self.G.remove_edge(3,4)
        return self.G

    def directed_graphs(self):
        """This function creates a directed graph.
        
        Returns
        -------
        Graph
            a nx directed graph with edges only
        """
        # Add edges to a directed graph (same as undirected graph)
        directedG = nx.DiGraph()
        directedG.add_edge(2,1) # adds the nodes in order 2, 1
        directedG.add_edge(1,3)
        directedG.add_edge(2,4)
        directedG.add_edge(1,2)
        # Add weighted edges
        directedG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
        return directedG

    def num_nodes(self, G):
        """This function gives the number of nodes in a graph.
        
        Returns
        -------
        int
            the number of nodes in a graph
        """
        # Find the number of nodes 
        return self.G.number_of_nodes()
    
    def num_edges(self, G):
        """This function gives the number of edges in a graph.
        
        Returns
        -------
        int
            the number of edges in a graph
        """
        # Find the number of edges
        return self.G.number_of_edges()

    def view_graph(self):
        """This function gives a list of the nodes and edges in a graph.
        
        Returns
        -------
        list
            a list of all the nodes in a graph
        list
            a list of all the edges in a graph
        """
        # View nodes
        nodes = list(self.G.nodes)
        # View edges
        edges = list(self.G.edges)
        return nodes, edges

    def construct_graph(self):
        """This function creates a graph from another graph.
        
        Returns
        -------
        Graph
            a directed graph
        """
        self.G.add_edge(5,6)
        # Create a directed graph using the connections from G
        newGraph = nx.DiGraph(self.G)
        return newGraph
    
    def construct_from_edges(self, newGraph):
        """This function creates a graph from a list of edges.
        
        Returns
        -------
        list
            a list of edges in a graph
        """
        # Create a graph from the list of edges in newGraph
        fromEdges = nx.Graph(list(newGraph.edges()))
        return list(fromEdges.edges())

    def construct_from_adj_dict(self):
        """This function creates a graph from an adjacency dictionary.
        
        Returns
        -------
        list
            a list of edges in a graph
        """
        adj_dict = {0: (1,2), 1: (0,2), 2: (0,1)}
        # Create a new graph from the adjacency dictionary (adj_dict)
        fromDict = nx.Graph(adj_dict)
        return list(fromDict.edges())

    def access_graph(self):
        """This function allows you to quickly access all (node, adjacency) pairs, as well as all edges"""
        graph = nx.Graph()
        graph.add_weighted_edges_from([(1,2,0.125), (1,3,0.75), (2,4,1.2), (3,4,0.375)])

        for n, neighbors in graph.adj.items():
            for neighbor, eattr in neighbors.items():
                weight = eattr['weight']
                if weight < 0.5:
                    print(f"({n}, {neighbor}, {weight:.3}")
        for (u, v, weight) in graph.edges.data('weight'):
            if weight < 0.5:
                print(f"({u}, {v}, {weight:.3}")

    def graph_attributes(self):
        """This function creates a graph with graph attributes.
        
        Returns
        -------
        graph
            a nx graph of days
        """
        # Assign graph attributes when creating a new graph
        day_graph = nx.Graph(day="Friday")
        # Modify attributes
        day_graph.graph['day'] = "Monday"
        return day_graph.graph
    
    def node_attributes(self, day_graph):
        """This function adds node attributes.
        
        Returns
        -------
        dict
            a dictionary of nodes and their attributes
        """
        # Add node attributes
        day_graph.add_node(1, time='5pm')
        day_graph.add_nodes_from([3], time='2pm')
        return day_graph.nodes.data()

    def edge_attributes(self, day_graph):
        """This function adds edges with various attributes.
        
        Returns
        -------
        dict
            a dictionary of edges and their attributes 
        """
        # Add edges with weight attribute
        day_graph.add_edge(1,2, weight=4.7)
        # Add edges with color attribute
        day_graph.add_edges_from([(3,4), (4,5)], color='red')
        day_graph.add_edges_from([(1,2, {'color': 'blue'}), (2,3, {'weight': 8})])
        return day_graph.edges.data()

    def multigraphs(self):
        """This function creates a graph that allows multiple edges between pairs of nodes
        
        Returns
        -------
        dict
            a dictionary of the shortest path between nodes
        """
        # Create a graph that allows multiple edges between any pair of nodes
        multigraph = nx.MultiGraph()
        multigraph.add_weighted_edges_from([(1,2,0.5), (1,2,0.75), (2,3,0.5)])
        # Get the dictionary of weights and edges for multigraph
        weightsAndEdges = dict(multigraph.degree(weight='weight'))
        # Create a normal graph
        graph = nx.Graph()

        for n, neighbors in multigraph.adjacency():
            for neighbor, edict in neighbors.items():
                minval = min([d['weight'] for d in edict.values()])
                graph.add_edge(n, neighbor, weight=minval)
        
        # find the shortest path between nodes
        shortestPath = nx.shortest_path(graph, 1, 3)
        return shortestPath

import unittest

class NetworkXTest(unittest.TestCase):
    """This class tests the functions in NetworkXTutorial."""

    def test_num_nodes(self):
        """This function tests the num_nodes function."""
        test_graph = nx.Graph()
        test_graph.add_nodes_from([(1,2),(3,4)])
        result = NetworkXTutorial.num_nodes(test_graph)
        self.assertEqual(result, 4)

    def test_num_edges(self):
        """This function tests the num_edges function."""
        test_graph = nx.Graph()
        test_graph.add_edges_from([(5,6),(7,8)])
        result = NetworkXTutorial.num_edges(test_graph)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()