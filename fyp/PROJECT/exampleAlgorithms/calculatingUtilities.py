import nashpy as nash
import numpy as np

A = np.array([[3,0], [5,1]])
B = np.array([[3,5],[0,1]])
prisoners_dilemma = nash.Game(A,B)

# The utility for both players when they both play their first action
sigma_r1 = np.array([1,0])
sigma_c1 = np.array([1,0])
print(prisoners_dilemma[sigma_r1, sigma_c1])

# The utility to both players when they play uniformly randomly across both their actions
sigma_r2 = np.array([1/2, 1/2])
sigma_c2 = np.array([1/2, 1/2])
print(prisoners_dilemma[sigma_r2, sigma_c2])

# Use the is_best_response method to return a pair of booleans 
sigma_r3 = np.array([0,1])
sigma_c3 = np.array([1,0])

print(prisoners_dilemma.is_best_response(sigma_r1, sigma_c1))
print(prisoners_dilemma.is_best_response(sigma_r2, sigma_c2))
print(prisoners_dilemma.is_best_response(sigma_r3, sigma_c3))