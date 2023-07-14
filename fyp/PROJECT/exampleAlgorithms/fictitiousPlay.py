import nashpy as nash
import numpy as np

class FictitiousPlay:
    """This class uses the fictitious play methods to generate learning steps for a game with two players.
    
    Attributes
    ----------
    A : array
        A NumPy array of payoffs
    B : array
        A NumPy array of payoffs

    Methods
    -------
    create_game()
        Creates a NashPy game of two players
    fictitious_play_game(game)
        Generates a collection of learning steps for the game passed
    passing_play_counts(game)
        Generates a collection of learning steps from the game passed by using a play_counts variable
    stochastic_fictitious_play(game)
        Generate a collection of learning steps from the game passed in a stochastic function
    stochastic_passing_play_counts(game)
        Generates a collection of learning steps from the game passed in a stoachatic function by using a play_counts variable
    etha_and_epsilon_bar(game)
        Generates a collection of learning steps from the game passed in a stochastic function by passing a value for etha and epsilon_bar
    """
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def create_game(self):
        """This function creates a game with two players.
        
        Returns
        -------
        game
            A NashPy game
        """
        self.A = np.array([[3,1],[0,2]])
        self.B = np.array([[2,0],[1,3]])
        game = nash.Game(self.A, self.B)
        return game

    def fictitious_play_game(self, game):
        """This function uses fictitious play to generate a collection of learning steps.
        
        Returns
        -------
        tuple
            A tuple of learning steps
        """
        # This is a stochastic process
        np.random.seed(0)
        iterations = 500
        play_counts = game.fictitious_play(iterations=iterations)

        for row_play_counts, column_play_counts in play_counts:
            return row_play_counts, column_play_counts

    def passing_play_counts(self, game):
        """This function uses fictitious play to generate a collection of learning steps by passing play_counts as a starting point for the algorithm.
        
        Returns
        -------
        tuple
            A tuple of learning steps 
        """
        np.random.seed(0)
        iterations = 500
        play_counts = (np.array([0.,500.]), np.array([0.,500.]))
        play_counts = game.fictitious_play(iterations=iterations, play_counts=play_counts)

        for row_play_counts, column_play_counts in play_counts:
            return row_play_counts, column_play_counts

    def stochastic_fictitious_play_game(self, game):
        """This function uses stochastic_fictitious_play to generat a collection of learning steps made up of the play counts and the mixed strategy of each player.

        Returns
        -------
        tuple
            A tuple of learning steps
        """
        np.random.seed(0)
        iterations = 500
        play_counts_and_distributions = game.stochastic_fictitious_play(iterations=iterations)

        for play_counts, distributions in play_counts_and_distributions:
            row_play_counts, column_play_counts = play_counts
            row_distributions, column_distributions = distributions
            return row_play_counts, column_play_counts, row_distributions, column_distributions

    def stochastic_passing_play_counts(self, game):
        """This function passes play_counts to the stochastic_fictitious_play function to generate a collection of learning steps.
        
        Returns
        -------
        tuple
            A tuple of learning steps
        """
        # possible to pass a play_counts variable to give a starting point for the algorithm
        np.random.seed(0)
        iterations = 500
        play_counts = (np.array([0.,500.]), np.array([0.,500.]))
        play_counts_and_distributions = game.stochastic_fictitious_play(iterations=iterations, play_counts=play_counts)

        for play_counts, distributions in play_counts_and_distributions:
            row_play_counts, column_play_counts = play_counts
            row_distributions, column_distributions = distributions
            return row_play_counts, column_play_counts

    def etha_and_epsilon_bar(self, game):
        """This function passes a value of etha and epsilon_bar to stochastic_fictitious_play method to generate a collection to learning steps.
        
        Returns
        -------
        tuple
            A tuple of learning steps
        """
        # a value for etha and epsilon_bar can be passed
        np.random.seed(0)
        iterations = 500
        etha = 10**-2
        epsilon_bar = 10**-3
        play_counts_and_distributions = game.stochastic_fictitious_play(iterations=iterations, etha=etha, epsilon_bar=epsilon_bar)

        for play_counts, distributions in play_counts_and_distributions:
            row_play_counts, column_play_counts = play_counts
            row_distributions, column_distributions = distributions
            return row_play_counts, column_play_counts