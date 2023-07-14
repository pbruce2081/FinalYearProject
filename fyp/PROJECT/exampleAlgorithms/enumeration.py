# The following code is from the NashPy documentation https://nashpy.readthedocs.io/en/stable/how-to/index.html

import nashpy as nash
import numpy as np

class Enumeration:
    """This class uses the enumeration functions provided by NashPy to calculate different equilibria for a matching pennies game.
    
    Attributes
    ----------
    A : array
        A NumPy array of payoffs

    Methods
    -------
    create_game()
        Creates a matching pennies game 
    support_enumeration(matching_pennies)
        Calculates the support equilibria for the matching pennies game
    vertext_enumeration(matching_pennies)
        Calculates the vertex equilibria for the matching pennies game
    solve_lemke_howson(matching_pennies)
        Uses the Lemke Howson algorithm to solve the equilibria of the matching pennies game
    """
    def __init__(self, A):
        """
        Parameters
        ----------
        A : array
            A NumPy array of payoffs
        """
        self.A = A

    def create_game(self):
        """This function creates a matching pennies game.
        
        Returns
        -------
        game
            A NashPy game containing the payoffs for the matching pennies game
        """
        # Create matching pennies game
        self.A = np.array([[1,-1], [-1,1]])
        matching_pennies = nash.Game(A)
        return matching_pennies
    
    def support_enumeration(self, matching_pennies):
        """This function calculates the support equilibria for the matching pennies game."""
        # support_enumeration method returns a generator of all the equilibria
        support_equilibria = matching_pennies.support_enumeration()

        for s_eq in support_equilibria:
            return s_eq

    def vertex_enumeration(self, matching_pennies):
        """This function calculates the vertex equilibria for the matching pennies game."""
        # vertex_enumeration method returns a generator of all the equilibria
        vertex_equilibria = matching_pennies.vertex_enumeration()

        for v_eq in vertex_equilibria:
            return v_eq

    def solve_lemke_howson(self, matching_pennies):
        """This function uses the Lemke Howson algorithm to solve the equilibria for the matching pennies game."""
        # Solve with Lemke Howson
        # This algorithm does not return all the equilibria and takes an input argument
        result = matching_pennies.lemke_howson(initial_dropped_label=0) # the initial_dropped_label is an int between 0 and sum(A.shape)-1
        print(result)
        # Iterate over all possible labels using the lemke_howson_enumeration()
        lemke_equilibria = matching_pennies.lemke_howson_enumeration()

        for l_eq in lemke_equilibria:
            return l_eq