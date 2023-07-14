import nashpy as nash
import numpy as np

class PrisonersDilemma:
    """This class creates a Prisoner's Dilemma game, calculayes each players' payoff and finds the best response for the game.
    
    Attributes
    ----------
    p1 : array
        A Numpy array of payoffs for Player 1 (union workers)
    p2 : array
        A Numpy array of payoffs for Player 2 (the government)
        
    Methods
    -------
    set_p1()
        Takes a user input for Player 1's payoffs and converts to numpy array
    set_p2()
        Takes a user input for Player 2's payoffs and converts to numpy array
    create_game(p1,p2)
        Creates a NashPy game
    calc_p1_sigma(p1)
        Calculates the sigma for Player 1
    calc_p2_sigma(p2)
        Calculates the sigma for Player 2
    calc_utils(sigma_p1, sigma_p2, prisoners_dilemma)
        Calculates the utilities of each player
    best_response(p1, p2, sigma_p1, sigma_p2)
        Calculates the best response based off the sigma of each player
    """
    def __init__(self, p1, p2):
        """
        Parameters
        ----------
        p1 : array
            A NumPy array of payoffs for Player 1
        p2 : array 
            A NumPy array of payoffs for Player 2
        """
        self.p1 = p1
        self.p2 = p2

    def set_p1_pd(entry_p1):
        """
        This function accepts a user input for Player 1's payoffs and converts it to a NumPy array.
        
        Returns
        -------
        Array
            An array of Player 1's payoffs
        """
        rows = 2
        columns = 2

        print("Enter the entries in a single line: ")
        p1_in = list(map(int, entry_p1.split()))
        p1 = np.array(p1_in).reshape(rows, columns)
        print(p1)
        return(p1)
    
    def set_p2_pd(entry_p2):
        """
        This function accepts a user input for Player 2's payoffs and converts it to a NumPy array.
        
        Returns
        -------
        Array
            An array of Player 2's payoffs
        """
        rows = 2
        columns = 2

        print("Enter the entries in a single line: ")
        p2_in = list(map(int, entry_p2.split()))
        p2 = np.array(p2_in).reshape(rows, columns)
        print(p2)
        return(p2)

    def create_pd_game(p1, p2):
        """This function creates the Prisoner's Dilemma game from the two players' payoff matrices.
        
        Returns
        -------
        game
            A NashPy game with two payoff matrices
        """

        # create the game from p1 and p2
        prisoners_dilemma = nash.Game(p1, p2)
        print("Prisoners Dilemma Game: \n", prisoners_dilemma)
        return prisoners_dilemma

    def calc_p1_sigma(p1):
        """This function calculates the sigma for Player 1
        
        Returns
        -------
        list
            A list of the utilities
        """

        # calculate utility 1 from the formula below
        util1 = p1[0][0]/(p1[0][0] + p1[1][1])
        # calculate utility 2 from 1-utility 1
        util2 = 1 - util1
        # assign Player 1's sigma to a list of the utilities
        sigma_p1 = [util1, util2]
        return sigma_p1

    def calc_p2_sigma(p2):
        """This function calculates the sigma for Player 2
        
        Returns
        -------
        list
            A list of the utilities
        """

        # calculate utility from the formula below
        util1 = p2[0][1]/(p2[0][1] + p2[1][0])
        # calculate utility 2 from 1-utility 1
        util2 = 1 - util1
        # assign Player 2's sigma to a list of the utilities
        sigma_p2 = [util1, util2]
        return sigma_p2
    
    def calc_utils(sigma_p1, sigma_p2, prisoners_dilemma):
        """This function calculates the utilities of the two players.
        
        Returns
        -------
        array
            An array of the utilities
        """

        # calculate the utilties by calling the game with the sigmas of each player
        utilities = prisoners_dilemma[sigma_p1, sigma_p2]
        print("Utilities: \n", utilities)
        return utilities

    def best_response(p1, p2, sigma_p1, sigma_p2):
        """This function calculates the best repsonse for the players.
        
        Returns
        -------
        array
            An array of the best response for each sigma
        """

        # calculate the best response for Player 1 
        best_resp_p1 = p2 * sigma_p2
        # calculate the best response for Player 2
        best_reps_p2 = sigma_p1 * p1
        print("Best Response for Player 1: \n", best_resp_p1)
        print("Best Response for Player 2: \n", best_reps_p2)
        return [best_resp_p1, best_reps_p2]

    def check_best_response(sigma_p1, sigma_p2, prisoners_dilemma):
        """This function checks to see if the best response is the actual best response
        
        Returns
        -------
        Boolean
            True or False 
        """

        # use the is_best_response function to calculate whether the best response we got is correct
        is_best = prisoners_dilemma.is_best_response(sigma_p1, sigma_p2)
        print("Is this the best response?\n", is_best)
        return is_best

if __name__ == "__main__":
    pd = PrisonersDilemma
    p1 = pd.set_p1_pd()
    p2 = pd.set_p2_pd()
    pd_game = pd.create_pd_game(p1, p2)
    sigma_p1 = pd.calc_p1_sigma(p1)
    sigma_p2 = pd.calc_p2_sigma(p2)
    utils = pd.calc_utils(sigma_p1, sigma_p2, pd_game)
    best_resp = pd.best_response(p1, p2, sigma_p1, sigma_p2)
    is_best = pd.check_best_response(sigma_p1, sigma_p2, pd_game)