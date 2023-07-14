import numpy as np
import nashpy as nash

A = np.array([[3,2],[4,2]])
game = nash.Game(A)

# the replicator_dynamics methods returns the strategies of the row player over time 
print(game.replicator_dynamics())

# it is also posible to pass a y0 variable which assigns a starting strategy
y0 = np.array([0.9, 0.1])

# passing a timepoints variable gives the algorithm a sequence of timepoints over which to calculate the strategies
timepoints = np.linspace(0,10,1000)
print(game.replicator_dynamics(y0=y0, timepoints=timepoints))

''' given  matrix Q such that Qij gives the probability that an individual of type i mutates
to an individual of type j, the replicator dynamics equation with mutation can be solved using the below'''

Q = np.array([[9 / 10, 1 / 10], [1 / 5, 4 / 5]])
print("Mutation Matrix:\n", game.replicator_dynamics(mutation_matrix=Q))

# asymmetric replicator dynamics 
B = np.array([[1,3],[2,4]])
game = nash.Game(A,B)

# the asymmetric_replicator_dynamics method returns the stratgies of both the row and column players over time
xs, ys = game.asymmetric_replicator_dynamics()
print("xs:\n", xs)
print("ys:\n", ys)

# x0 and y0 can be passed to assign the initial strategy to be played 
x0 = np.array([0.4, 0.6])
y0 = np.array([0.9, 0.1])

# a timepoints argument can be passed 
xs, ys = game.asymmetric_replicator_dynamics(x0=x0, y0=y0, timepoints=timepoints)
print("xs:\n", xs)
print("ys:\n", ys)