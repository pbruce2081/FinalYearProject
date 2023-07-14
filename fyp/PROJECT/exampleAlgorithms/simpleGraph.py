import networkx as nx
import matplotlib.pyplot as plt

class SimpleGraph:
    """This class creates a simple graph with 5 edges and displays it using matplotlib.
    
    Attributes
    ----------
    simpleGraph : Graph
        A NetworkX graph

    Methods
    -------
    create_graph()
        Creates and displays a graph
    """
    def __init__(self, simpleGraph):
        """
        Parameters
        ----------
        simpleGraph : Graph
            A NetworkX graph
        """
        self.simpleGraph = simpleGraph

    def create_graph():
        """This function creates and displays a simple graph.
        
        Returns
        -------
        None
        """
        # Create a graph
        simpleGraph = nx.Graph()

        # Add nodes
        simpleGraph.add_edge(1,2)
        simpleGraph.add_edge(1,5)
        simpleGraph.add_edge(2,4)
        simpleGraph.add_edge(2,3)
        simpleGraph.add_edge(4,5)
        simpleGraph.add_edge(3,4)
        simpleGraph.add_edge(1,4)

        # Add attributes of the graph
        options = {
            "node_size": 3000,
            "node_color": "white",
            "edgecolors": "pink",
            "linewidths": 5,
            "width": 5,
        }

        # Draw the graph
        nx.draw(simpleGraph, **options)

        # Set margins for the axes
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        # Show the graph
        plt.show()

graph = SimpleGraph
graph.create_graph()