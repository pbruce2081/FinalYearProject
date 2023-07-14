# This code example is taken from https://towardsdatascience.com/an-introduction-to-game-theory-using-python-358c63e36e02 

import numpy as np
import nashpy as nash

class PrisonersDilemma:
    """This class creates the Prisoner's Dilemma game and calculates their payoffs.
    
    Attributes
    ----------
    prisoner1 : array
        A NumPy array for the player's payoff
    prisoner2 : array
        A NumPy array for the player's payoff

    Methods
    -------
    create_game()
        Creates the game for both prisoner 1 and prisoner 2 using NashPy
    draw_tables()
        Draws the prisoners' payoffs in a more readable way using QuantEcon
    calculate_payoffs(x,y)
        Calculates the payoffs for the prisoners based on what they play
    """
    def __init__(self, prisoner1, prisoner2):
        """
        Parameters
        ----------
        prisoner1 : array
            The payoff matrix for prisoner 1
        prisoner2 : array
            The payoff matrix for prisoner 2
        """
        self.prisoner1 = prisoner1
        self.prisoner2 = prisoner2
    
    def create_game(prisoner1, prisoner2):
        """This function creates the payoff arrays for both prisoner 1 and prisoner 2.
        
        Returns
        -------
        game
            A NashPy game of the prisoners' payoffs
        """
        prisoners_dilemma = nash.Game(prisoner1, prisoner2)
        return prisoners_dilemma

    def calculate_payoffs(x=str, y=str):
        """This function calculates the payoffs of the prisoners' based off what they choose to play.
        
        Returns
        -------
        list
            A list of payoffs
        """
        if x == 'noConfession' and y == 'noConfession':
            return [-1,-1]
        elif x == 'noConfession' and y == 'confession':
            return [-10, 0]
        elif x == 'confession' and y == 'confession':
            return [-9, -9]
        return [0, -10]

class PrisonersDilemmaTest:
    def test_create_game():
        test_prisoner1 = np.array([[-1,-10], [0, -9]])
        test_prisoner2 = test_prisoner1.T
        test_game = PrisonersDilemma.create_game(test_prisoner1, test_prisoner2)
        assert test_game

    def test_confession_no_confession():
        test_x = 'confession'
        test_y = 'noConfession'
        test_payoff = PrisonersDilemma.calculate_payoffs(test_x, test_y)
        assert test_payoff == [0, -10]

    def test_no_confession():
        test_x = 'noConfession'
        test_y = 'noConfession'
        test_payoff = PrisonersDilemma.calculate_payoffs(test_x, test_y)
        assert test_payoff == [-1,-1]

test = PrisonersDilemmaTest
test.test_create_game()
test.test_confession_no_confession()
test.test_no_confession()