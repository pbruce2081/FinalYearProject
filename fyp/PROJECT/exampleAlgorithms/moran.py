import nashpy as nash
import numpy as np

A = np.array([[3,1], [1,2]])
game = nash.Game(A)

# the moran_process method returns a generator of a given collection of generations
np.random.seed(0)
generations = game.moran_process(initial_population=(0,0,1))

print("\nRandom Seed = 0:")
for population in generations:
    print(population)

# this is a stochastic process
np.random.seed(2)
generations = game.moran_process(initial_population=(0,0,1))

print("\nRandom Seed = 2:")
for population in generations:
    print(population)

# mutation_probability can be passed (will not terminate)
number_of_generations = 5
mutation_probability = 1
generations = game.moran_process(initial_population=(0,0,1), mutation_probability=mutation_probability)

print("\nMutation Probability:")
for _ in  range(number_of_generations):
    print(next(generations))