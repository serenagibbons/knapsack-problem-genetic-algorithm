from genetic_algorithm import genetic_algorithm

def main():
    # Set maximum weight capacity
    capacity = 250
    
    # Define items (weight, value)
    items = [
        {'weight': 20, 'value': 6},
        {'weight': 30, 'value': 5},
        {'weight': 60, 'value': 8},
        {'weight': 90, 'value': 7},
        {'weight': 50, 'value': 6},
        {'weight': 70, 'value': 9},
        {'weight': 30, 'value': 4},
        {'weight': 30, 'value': 5},
        {'weight': 70, 'value': 4},
        {'weight': 20, 'value': 9},
        {'weight': 20, 'value': 2},
        {'weight': 60, 'value': 1}
    ]

    # Hyperparameters for the genetic algorithm
    population_size = 100
    convergence_rate = 0.75
    culling_rate = 0.5
    mutation_rate = 0.05
    
    # Run the genetic algorithm
    best_chromosome, best_weight, best_value = genetic_algorithm(items, capacity, population_size, culling_rate, mutation_rate, convergence_rate)

    # Print the results
    print(f"Best chromosome: {best_chromosome}")
    print(f"Total weight: {best_weight}")
    print(f"Total value: {best_value}")

if __name__ == "__main__":
    main()