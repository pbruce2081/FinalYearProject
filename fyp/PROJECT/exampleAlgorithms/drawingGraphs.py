# The code in this file comes from the NetworkX Tutorial page https://networkx.org/documentation/stable/tutorial.html

import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class DrawingGraphs:
    """This class creates and draws various graphs using NetworkX and matplotlib.
    
    Attributes
    ----------
    G : Graph
        a NetworkX graph

    Methods
    -------
    draw_petersen_graph()
        Draws and displays two petersen graphs
    draw_graphs()
        Draws and displays four different shaped graphs from a petersen graph
    draw_dodecahedral_graph()
        Draws and displays a dodecahedral graph and saves it to a file
    """
    def __init__(self, G):
        self.G = G
    
    def draw_petersen_graph(self):
        """This function draws two graphs from a petersen graph"""
        # Create a petersen graph
        self.G = nx.petersen_graph()
        # Create a sub-axis
        subax1 = plt.subplot(121)
        # Draw the graph using the NetworkX draw function
        nx.draw(self.G, with_labels=True, font_weight='bold')
        # Create a second sub-axis
        subax2 = plt.subplot(122)
        # Draw a second graph
        nx.draw_shell(self.G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
        plt.show()
    
    def draw_graphs(self):
        """This function creates four graphs of different shapes."""
        # Create a graph
        self.G = nx.petersen_graph()
        # Set the node color, size and width
        options = {
            'node_color': 'pink',
            'node_size': 100,
            'width': 3,
        }
        # Create a sub-plot
        subax1 = plt.subplot(221)
        # Draw a randomly shaped graph
        nx.draw_random(self.G, **options)
        # Create a sub-plot
        subax2 = plt.subplot(222)
        # Draw a circular graph
        nx.draw_circular(self.G, **options)
        # Create a sub-plot
        subax3 = plt.subplot(223)
        # Draw a spectral graph
        nx.draw_spectral(self.G, **options)
        # Create a sub-plot
        subax4 = plt.subplot(224)
        # Draw a shell-shaped graph
        nx.draw_shell(self.G, nlist=[range(5,10), range(5)], **options)
        plt.show()

    def draw_dodecahedral_graph(self):
        """This function creates and draws a dodecaherdal graph and saves it."""
        # Create a dodecaherdal graph
        self.G = nx.dodecahedral_graph()
        # Set the node color, size and width
        options = {
            'node_color': 'purple',
            'node_size': 100,
            'width': 3,
        }
        # Create a list of shells
        shells = [
            [2,3,4,5,6],
            [8,1,0,19,18,17,16,15,14,7],
            [9,10,11,12,13]
        ]
        nx.draw_shell(self.G, nlist=shells, **options)
        plt.show()
        # Save the graph to a file
        plt.savefig("dodecahedralGraph.png")

mygraph = DrawingGraphs(nx.Graph())
mygraph.draw_petersen_graph()
mygraph.draw_graphs()
mygraph.draw_dodecahedral_graph()