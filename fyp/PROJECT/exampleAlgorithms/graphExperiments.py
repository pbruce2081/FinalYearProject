import networkx as nx
import matplotlib.pyplot as plt

class GraphExperiements:
    """This class creates and displays a series of interesting graphs.

    These graphs include: les_miserables_graph, florentine_families_graph and caveman_graph.

    Methods
    -------
    les_mis_graph_example()
        Creates and displays a graph containing the relationships between all the characters in Les Miserables
    floretine_families_graph_example()
        Creates and displays a graph containing the relationships between Florentine families
    caveman_graph_example()
        Creates and displays a graph that shows the reltionship within cavemen tribes
    """
    def les_mis_graph_example():
        """This function creates and displays a graph containing the relationships between all the characters in Les Miserables.
        
        Returns
        -------
        None
        """
        les_mis = nx.les_miserables_graph()

        options = {
            "node_color": "blue",
            "edgecolors": "red",
            "node_size": 500,
            "width": 5
        }

        nx.draw_spring(les_mis, alpha=0.2, font_size=10, with_labels=True, **options)
        plt.show() 

    def florentine_families_graph_example():
        """This function creates and displays a graph containing the relationships between the families in Florence.
        
        Returns
        -------
        None
        """
        florentine_families = nx.florentine_families_graph()

        options = {
            "node_color": "green",
            "edgecolors": "red",
            "node_size": 500,
            "width": 5
        }

        nx.draw(florentine_families, alpha=0.2, font_size=10, with_labels=True, **options)
        plt.show()

    def caveman_graph_example():
        """This function creates and displays the relationships within cavemen tribes (but not with other tribes).
        
        Returns
        -------
        None
        """
        cavemen = nx.caveman_graph(10, 10)

        options = {
            "node_color": "brown",
            "edgecolors": "grey",
            "node_size": 500,
            "width": 5
        }

        nx.draw(cavemen, alpha=0.2, font_size=10, with_labels=True, **options)
        plt.show()

graph = GraphExperiements
graph.les_mis_graph_example()
graph.florentine_families_graph_example()
graph.caveman_graph_example()