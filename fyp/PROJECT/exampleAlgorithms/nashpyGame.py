import nashpy as nash
import numpy as np

class NashPyGame:
    """This class goes through the simple NashPy Game on https://nashpy.readthedocs.io/en/stable/tutorial/index.html

    Attributes
    ----------
    A : array
        a NumPy array to represent a game

    Methods
    -------
    create_games()
        Creates a simple game.
    create_same_game(A)
        Creates a game from a pair of matrices
    calculate_utilities(rps)
        Calculate the utilities payoffs earned during the game
    calculate_random_utilities(rps)
        Calculate the utilities after a random sigma 
    compute_nash_equilibrium(rps)
        Compute the Nash equilibrium of a game
    learning_games(rps)
        Learn during a game 
    """

    def __init__(self, A):
        """
        Parameters
        ----------
        A : array
            A NumPy array
        """
        self.A = A

    def create_games(self):
        """This function creates a simple game from one matrix.
        
        Returns
        -------
        game
            A NashPy Game object
        """
        # Create a simple game
        self.A = np.array([[0,-1,1], [1,0,-1], [-1,1,0]])
        rps = nash.Game(self.A)
        return rps

    def create_same_game(self):
        """This function creates a game from a pair of matrices.
        
        Returns
        -------
        game
            A NashPy Game object
        """
        # Pass a pair of matrices to create the same game (-A)
        B = -self.A
        rps2 = nash.Game(self.A,B)
        return rps2

    def calculate_utilities(self, rps):
        """This function calculates the utility payoff for a game.
        
        Returns
        -------
        tuple
            A tuple of the utility payoff 
        """
        sigma_r = [0,0,1]
        sigma_c = [0,1,0]
        return "Payoff: ", rps[sigma_r, sigma_c]

    def calculate_random_utilities(self, rps):
        """This function calculates the utility payoff for random game.
        
        Returns
        -------
        tuple
            A tuple of the random utility payoff
        """
        sigma_c_rand = [1/2, 1/2, 0]
        sigma_r_rand = [0, 1/2, 1/2]
        return "Random Payoff: ", rps[sigma_r_rand, sigma_c_rand]

    def compute_nash_equilibrium(self, rps):
        """This function computes the Nash equilibrium of a game.
        
        Returns
        -------
        list
            A list containing the Nash equilibrium of a game
        """
        eqs = rps.support_enumeration()
        nashEq = list(eqs)
        return nashEq

    def learning_games(self, rps):
        """This function uses fictitious play to learn during a game.
        
        Returns
        -------
        tuple
            A tuple containing the the learning steps
        """
        iterations = 100
        np.random.seed(0)
        play_counts = rps.fictitious_play(iterations=iterations)

        for row_play_count, column_play_count in play_counts:
            return(row_play_count, column_play_count)