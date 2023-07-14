import nashpy as nash
import numpy as np

class BattleOfTheSexes:
    """This class creates a battle of the sexes game, calculates each player's payoff and finds the best repsonse for the game.
    
    Attributes
    ----------
    p1 : array
        A NumPy array of payoffs for Player 1 (union workers)
    p2 : array
        A NumPy array of payoffs for Player 2 (the government)
        
    Methods
    -------
    set_p1()
        Takes a user input for player 1's payoffs and converts to numpy array
    set_p2()
        Takes a user input for player 2's payoffs and converts to numpy array
    create_game(p1, p2)
        Creates a NashPy game
    calc_p1_sigma(p1)
        Calculates the sigma for Player 1
    calc_p2_sigma(p2)
        Calculates the sigma for Player 2
    calc_utils(sigma_p1, sigma_p2, battle_of_the_sexes)
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

    def set_p1_bos(p1_entry):
        """
        This function accepts a user input for player 1's payoffs and converts it to a numpy array
        
        Returns
        -------
        Array
            An array of player 1's payoffs
        """
        rows = 2
        columns = 2

        print("Enter the entries in a single line: ")
        p1_in = list(map(int, p1_entry.split()))
        p1 = np.array(p1_in).reshape(rows, columns)
        print(p1)
        return(p1)
    
    def set_p2_bos(p2_entry):
        """
        This function accepts a user input for player 2's payoffs and converts it to a numpy array
        
        Returns
        -------
        Array
            An array of player 2's payoffs
        """
        rows = 2
        columns = 2

        print("Enter the entries in a single line: ")
        p2_in = list(map(int, p2_entry.split()))
        p2 = np.array(p2_in).reshape(rows, columns)
        print(p2)
        return(p2)

    def create_bos_game(p1, p2):
        """This function creates the Battle of the Sexes game from the two players' payoff matrices.
        
        Returns
        -------
        game
            A NashPy game with two payoff matrices
        """

        # create the game from p1 and p2
        battle_of_the_sexes = nash.Game(p1, p2)
        print("Battle of the Sexes Game: \n", battle_of_the_sexes)
        return battle_of_the_sexes
    
    def calc_p1_sigma(p1):
        """This function calculates the sigma for Player 1.
        
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
        """This function calculates the sigma for Player 2.
        
        Returns
        -------
        list
            A list of the utilities
        """

        # calculate utility 1 from the formula below
        util1 = p2[0][1]/(p2[0][1] + p2[1][0])
        # calculate utility 2 from 1-utility 1
        util2 = 1 - util1
        # assign Player 2's sigma to a list of the utilities
        sigma_p2 = [util1, util2]
        return sigma_p2

    def calc_utils(sigma_p1, sigma_p2, battle_of_the_sexes):
        """This function calculates the utilities of the two players.
        
        Returns
        -------
        array
            An array of the utilities
        """

        # calculate the utilties by calling the game with the sigmas of each player
        utilities = battle_of_the_sexes[sigma_p1, sigma_p2]
        print("Utilities: \n", utilities)
        return utilities
    
    def best_response(p1, p2, sigma_p1, sigma_p2):
        """This function calculates the best repsonse for the players.
        
        Returns
        -------
        array
            An array of the best response for each sigma
        """

        # calculate the best response for Player 1
        best_resp_p1 = p2 * sigma_p2
        # calculate the best response for Player 2
        best_resp_p2 = sigma_p1 * p1
        print("Best Response for Player 1: \n", best_resp_p1)
        print("Best Response for Player 2: \n", best_resp_p2)
        return [best_resp_p1, best_resp_p2]

if __name__ == "__main__":
    bos = BattleOfTheSexes
    p1 = bos.set_p1_bos()
    p2 = bos.set_p2_bos()
    bos_game = bos.create_bos_game(p1, p2)
    sigma_p1 = bos.calc_p1_sigma(p1)
    sigma_p2 = bos.calc_p2_sigma(p2)
    utils = bos.calc_utils(sigma_p1, sigma_p2, bos_game)
    best_resp = bos.best_response(p1, p2, sigma_p1, sigma_p2)