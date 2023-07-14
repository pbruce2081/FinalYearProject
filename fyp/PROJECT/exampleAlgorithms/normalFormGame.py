import nashpy as nash
import numpy as np

A = np.array([[1,-1], [-1,1]])
matching_pennies = nash.Game(A)
# Creates a zero sum game 
print(matching_pennies)

# non-zero sum game
B = np.array([[3,0], [5,1]])
C = np.array([[3,5],[0,1]])
prisoners_dilemma = nash.Game(B,C)
print(prisoners_dilemma)