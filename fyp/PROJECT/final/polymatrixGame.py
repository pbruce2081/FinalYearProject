import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class PolymatrixGame:
    """This class creates a polymatrix game, calculates the payoffs of every player, calculates the best response, gets the best response and the nash equilibria and draws the graph using NetworkX.
    
    Attributes
    ----------
    num_players : int
        An integer of the number of players
        
    Methods
    -------
    generate_payoffs()
        Generates the payoffs from the number of players
    generate_strategies()
        Generates the strategies of each player
    calc_best_response()
        Calculates the best response for a player based on their strategy
    get_nash_equilibria()
        Gets the nash equilibria available in the graph
    draw_graph()
        Draws the graph of the game
    """
    def __init__(self):
        """
        Parameters
        ----------
        payoffs : array
            A NumPy array of payoffs for each player
        num_players : int
            An integer of the number of players 
        strategies : array
            A NumPy array of zeros for the strategies of each player
        """
       # self.num_players = num_players
        self.payoffs = self.generate_payoffs()
        self.strategies = self.generate_strategies()

    def generate_payoffs(num_players):
        """This function generates the payoffs from the number of players.
        
        Returns
        -------
        list:
            A list of payoffs
        """
        # create a list of payoffs
        payoffs_list = []
        # iterate through all players
        for i in range(int(num_players)):
            # create a temporary list
            temp = []
            # iterate through all players
            for j in range(int(num_players)):
                # append the sum of index i + index j + 1 and mod it by the number of players
                temp.append((i+j+1) % int(num_players))
            # append temp to the list of payoffs
            payoffs_list.append(temp)
        payoffs = np.array(payoffs_list)
        return payoffs
    
    def generate_strategies(num_players):
        """This function generates the strategies of each player from the number of players.
        
        Returns
        -------
        list:
            A list of strategies
        """
        # create a list of strategies
        strategies_list = []
        # iterate through all players
        for i in range(int(num_players)):
            # append a list in the range of the number of players
            strategies_list.append(list(range(int(num_players))))
        strategies = np.array(strategies_list)
        return strategies
    
    def calc_best_response(num_players, payoffs):
        """This function calculates the best response for a player based on the strategy.
        
        Returns
        -------
        list:
            A list of best responses
        """
        # create a list of best responses 
        best_responses = []

        # iterate through all players
        for i in range(int(num_players)):
            # append the indices of the max element of payoffs
            best_responses.append(np.argmax(payoffs[i,:]))

        return best_responses
    
    def get_nash_equilibria(strategies, num_players, payoffs):
        """This function gets the nash equilibria available within the graph of games
        
        Returns
        -------
        list
            A list of all nash equilibria
        """

        # calculate the number of strategies
        num_strategies = strategies.shape[0]

        # create a list of nash equilibria 
        nash_equilibria = []

        # iterate through all strategies
        for i in range(int(num_strategies)):
            # create boolean variable
            is_nash_equil = True
            # iterate through all players
            for j in range(int(num_players)):
                # call function to calculate best responses
                br = PolymatrixGame.calc_best_response(num_players, payoffs)
                # check that the payoffs at indices j and i is less than those at indices j and br[i]
                if payoffs[j,i] < payoffs[j, br[i]]:
                    # no nahs equilibrium, so set to false
                    is_nash_equil = False
                    break
            # check if it is a nash equilibrium
            if is_nash_equil:
                # add to list
                nash_equilibria.append(i)
        return nash_equilibria
    
    def draw_graph(num_players, strategies, payoffs):
        """This function draws the graph of the polymatrix game.
        
        Returns
        -------
        None
        """

        # create a directed graph
        G = nx.DiGraph()
        # iterate through all players twice
        for i in range(int(num_players)):
            for j in range(int(num_players)):
                # check if i is not equal to j
                if i != j:
                    # iterate through strategies at index i
                    for k in strategies[i]:
                        # iterate through strategies at index j
                        for l in strategies[j]:
                            # set payoffs
                            payoff = payoffs[i][l] + payoffs[j][k]
                            # add edges
                            G.add_edge((i,k), (j,l), weight=payoff)
        # set position of nodes
        pos = nx.spring_layout(G)
        # create a dictionary of labels
        labels = {}
        # iterate through all nodes in the graph
        for node in G.nodes():
            # create lables for each player
            labels[node] = f"Player{node[0]+1}:{node[1]+1}"
        # draw the nodes
        nx.draw_networkx_nodes(G, pos, node_color='pink')
        # draw the egdes
        nx.draw_networkx_edges(G, pos)
        # draw the labels
        nx.draw_networkx_labels(G, pos, labels)
        # display the graph
        plt.show()

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game = PolymatrixGame(num_players)
    print(f"Payoffs: {game.payoffs}")
    print(f"Strategies: {game.strategies}")
    print(f"Best Response: {game.calc_best_response()}")
    print(f"Nash Equilibrium: {game.get_nash_equilibria()}")
    game.draw_graph()