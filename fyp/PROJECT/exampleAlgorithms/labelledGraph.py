# This example is from https://networkx.org/documentation/stable/auto_examples/drawing/plot_labels_and_colors.html#sphx-glr-auto-examples-drawing-plot-labels-and-colors-py 

import networkx as nx
import matplotlib.pyplot as plt

class LabelledGraphs:
    """This class creates and displays a graph with labelled and coloured nodes and edges.
    
    Attributes
    ----------
    graph : Graph
        A NetworkX graph

    Methods
    -------
    create_graph()
        Creates and displays a graph
    """
    def __init__(self, graph):
        """
        Parameters
        ----------
        graph : Graph
            A NetworkX graph
        """
        self.graph = graph

    def create_graph():
        """This function creates and displays a graph with coloured and labelled edges and nodes.
        
        Returns
        -------
        None
        """
        # Create graph
        graph = nx.cubical_graph()

        # Set position for all nodes
        node_pos = nx.spring_layout(graph, seed=1213764454)

        # Create nodes
        options = {
            "edgecolors": "grey",
            "node_size": 800,
            "alpha": 0.9
        }

        nx.draw_networkx_nodes(graph, node_pos, nodelist=[0,1,2,3], node_color="purple", **options)
        nx.draw_networkx_nodes(graph, node_pos, nodelist=[4,5,6,7], node_color="pink", **options)

        # Create edges
        nx.draw_networkx_edges(graph, node_pos, width=1.0, alpha=0.5)
        nx.draw_networkx_edges(graph, node_pos, edgelist=[(0,1), (1,2), (2,3), (3,0)], width=8, alpha=0.5, edge_color="purple")
        nx.draw_networkx_edges(graph, node_pos, edgelist=[(4,5), (5,6), (6,7), (7,4)], width=8, alpha=0.5, edge_color="pink")

        # Create labels
        labels = {}
        labels[0] = 'a'
        labels[1] = 'b'
        labels[2] = 'c'
        labels[3] = 'd'
        labels[4] = 'e'
        labels[5] = 'f'
        labels[6] = 'g'
        labels[7] = 'h'


        nx.draw_networkx_labels(graph, node_pos, labels, font_size=20, font_color="white")

        plt.tight_layout()
        plt.axis("off")
        plt.show()

graph = LabelledGraphs
graph.create_graph()