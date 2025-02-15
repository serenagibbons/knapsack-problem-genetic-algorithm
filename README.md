# Genetic Algorithm: The Knapsack Problem

You are going on a hiking trip, and there is a limit to the things you can bring. You have two things: a backpack with a size (the weight it can hold that is) and a set of boxes with different weights and different importance values.

The goal is to fill the backpack to make it as valuable as possible without exceeding the maximum weight (250):

## The Knapsack Probelm as a Genetic Algorithm
- Genetic representation: discrete bit-representation of all of the items that are included in the knapsack (1 for included, 0 for not included)
- Initial population: begin with a set of k randomly generated states
    - Set the population size to 100 to create a diverse population
- Selection: allocating individuals for reproduction
    - Truncated rank-based selection (Culling): selecting the top 50% of individuals in the ranked list and producing the same number of offspring for each selection
    - Parent individuals are randomly selected from the culled (top 50%) population.
- Genetic operators (fringe operations): modify the phenotype to obtain a new individual
    - Mutation: insert a single-point mutation at a small percentage (0.05) to modify a single gene of an individual
    - Crossover: given two individuals, produce two new ones that have elements of each by randomly selecting a point on each of the two individuals and swapping the genetic material around this point
- Fitness function: the total value of the chromosome
- Termination: the population converges when 80% of the chromosomes in the population have obtained the same fitness value

## Instructions
Run the program in the command line or terminal using the command `python main.py` in the root directory of the project.