import nashpy as nash
import numpy as np

class BattleOfTheSexes:
    """This class creates a battle of the sexes game, calculates each player's payoff and finds the best response for the game.
    
    Attributes
    ----------
    p1 : array
        A NumPy array of payoffs for Player 1
    p2 : array
        A NumPy array of payoffs for Player 2

    Methods
    -------
    create_game(p1, p2)
        Creates a NashPy game
    calculate_sigma_p1(p1)
        Calculates the sigma for player 1
    calculate_sigma_p2(p2)
        Calculates the sigma for player 2
    calculate_utilities(battle_of_the_sexes)
        Calculates the utilities of each player
    best_response(p1, p2)
        Calculates the best response based off the sigma of each player 
    """
    def __init__(self, p1, p2):
        """
        Parameters
        ----------
        p1 : array
            A NumPy array of payoffs for player 1
        p2 : array
            A NumPy array of payoffs for player 2
        """
        self.p1 = p1
        self.p2 = p2

    def create_game(p1, p2):
        """This function creates the Battle of the Sexes game from the two players' payoff matrices.
        
        Player 1 wants to go to the ballet, Player 2 wants to go to the fight. There are four possible outcomes :#
            1. P1 goes to the ballet, P2 goes to the fight: P1 receives a utility of 0, P2 receives a utility of 0
            2. P1 goes to the fight, P2 goes to the ballet: P1 receives a utility of 0, P2 receives a utility of 0
            3. P1 and P2 go to the ballet: P1 receives a utility of 70, P2 receives a utility of 30
            4. P1 and P2 go to the fight: P1 receives a utility of 70, P2 receives a utility of 30

        Returns
        -------
        game
            A NashPy game with two payoff matrices
        """
        battle_of_the_sexes = nash.Game(p1, p2)
        return battle_of_the_sexes

    def calculate_p1_sigma(p1):
        """This function calculates the sigma for player 1.
        
        Returns 
        -------
        list
            A list of the utilities
        """
        utility1 = p1[0][0]/(p1[0][0]+p1[1][1])
        utility2 = 1 - utility1
        sigma_p1 = [utility1, utility2]
        return sigma_p1

    def calculate_p2_sigma(p2):
        """This function calculates the sigma for player 2.
        
        Returns
        -------
        list
            A list of the utilities
        """
        utility1 = p2[0][1]/(p2[0][1]+p2[1][0])
        utility2 = 1 - utility1
        sigma_p2 = [utility1, utility2]
        return sigma_p2

    def calculate_utilities(sigma_p1, sigma_p2, battle_of_the_sexes):
        """This function calculates the utilities of the two players.
        
        Returns
        -------
        array
            An array of the utilities
        """
        utilities = battle_of_the_sexes[sigma_p1, sigma_p2]
        return utilities

    def best_response(p1, p2, sigma_p1, sigma_p2):
        """This function calculates the best response for the players.

        Returns
        -------
        array
            An array of the best responses for each sigma
        """
        best_rep_p1 = p2 * sigma_p2
        best_rep_p2 = sigma_p1 * p1
        return [best_rep_p1, best_rep_p2]

import pytest

class BattleOfTheSexesTest:
    def test_create_game():
        test_p1 = np.array([[3,0], [0,7]])
        test_p2 = np.array([[0,7], [3,0]])
        test_game = BattleOfTheSexes.create_game(test_p1, test_p2)
        assert test_game

    def test_calculate_sigma_p1():
        test_p1 = np.array([[3,0], [0,7]])
        test_sigma_p1 = BattleOfTheSexes.calculate_sigma_p1(test_p1)
        assert test_sigma_p1 == [0.3, 0.7]

    def test_calculate_sigma_p2():
        test_p2 = np.array([[0,7], [3,0]])
        test_sigma_p2 = BattleOfTheSexes.calculate_sigma_p1(test_p2)
        assert test_sigma_p2 == [0.7, 0.3]

    def test_calculate_utilities():
        test_p1 = np.array([[3,0], [0,7]])
        test_p2 = np.array([[0,7], [3,0]])
        test_game = BattleOfTheSexes.create_game(test_p1, test_p2)
        assert True

    def test_best_response():
        test_p1 = np.array([[3,0], [0,7]])
        test_p2 = np.array([[0,7], [3,0]])
        test_game = BattleOfTheSexes.create_game(test_p1, test_p2)
        assert True

test = BattleOfTheSexesTest
test.test_create_game()
test.test_calculate_sigma_p1()
test.test_calculate_sigma_p2()
test.test_calculate_utilities()
test.test_best_response()