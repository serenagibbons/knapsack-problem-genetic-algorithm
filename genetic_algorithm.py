import random

def generate_population(population_size, item_count):
    """
    Generates a random population of chromosomes.
    """
    population = [] 
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(item_count)]
        population.append(chromosome)

    return population

def calculate_fitness(chromosome, weights, values, capacity):
    """
    Calculates the fitness score of a chromosome.
    """
    total_weight = 0
    total_value = 0
    
    for i, gene in enumerate(chromosome):
        if gene == 1:
            total_weight += weights[i]
            if total_weight <= capacity:
                total_value += values[i]
            else:
                # Return if weight limit is exceeded
                return 0
    
    return total_value

def cull_population(population, fitnesses, truncation_percent):
    """
    Performs truncated rank-based selection.
    """
    # Sort the population by fitness in descending order (best to worst)
    sorted_indices = sorted(range(len(fitnesses)), key=lambda k: fitnesses[k], reverse=True)
    sorted_population = [population[i] for i in sorted_indices]
    sorted_fitnesses = [fitnesses[i] for i in sorted_indices]

    # Determine the truncation point
    truncation_point = int(truncation_percent * len(population))

    # Select the top individuals and fitnesses
    selected_population = sorted_population[:truncation_point]
    selected_fitnesses = sorted_fitnesses[:truncation_point]

    return selected_population, selected_fitnesses

def select_parents(population):
    """
    Randomly selects two chromosomes for reproduction.
    """
    population_size = len(population)
    parent1 = population[random.randint(0, population_size - 1)]
    parent2 = population[random.randint(0, population_size - 1)]

    return parent1, parent2

def crossover(parent1, parent2, crossover_point):
    """
    Performs one-point crossover on parent chromosomes.
    """
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

def mutate(chromosome, mutation_rate):
    """
    Performs a single-point mutation on a chromosome with a given probability.
    """
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
            break
    
    return chromosome

def popluation_converges(population, weights, values, capacity, convergence_rate):
    """
    Determines if a specified percentage of the population has the same fitness value (the population has converged).
    """
    fitness_values = {}
    for chromosome in population:
        fitness = calculate_fitness(chromosome, weights, values, capacity)
        fitness_values[fitness] = fitness_values.get(fitness, 0) + 1
    
    for fitness in fitness_values:
        if fitness_values[fitness]/len(population) > convergence_rate:
            return True

    return False

def genetic_algorithm(items, capacity, population_size, culling_rate, mutation_rate, convergence_rate):
    """
    Solve the knapsack problem using a genetic algorithm.
    """
    weights = [item['weight'] for item in items]
    values = [item['value'] for item in items]
    population = generate_population(population_size, len(items))

    population_coverged = False

    while not population_coverged:
        # Calculate fitnesses of each chromosome
        fitnesses = [calculate_fitness(chromosome, weights, values, capacity) for chromosome in population]

        # Cull the population
        population, fitnesses = cull_population(population, fitnesses, culling_rate)

        children = []
        for i in range(len(population)//2):
            # Select parents
            parent1, parent2 = select_parents(population)

            # Crossover
            crossover_point = random.randint(1, len(parent1) - 1)
            child1, child2 = crossover(parent1, parent2, crossover_point)

            # Mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            
            # Add children to children list
            children.extend([child1, child2])

        # Add children to population
        population.extend(children)

        population_coverged = popluation_converges(population, weights, values, capacity, convergence_rate)
    
    # Find the best chromosome in the final population
    best_chromosome_index = fitnesses.index(max(fitnesses))
    best_chromosome = population[best_chromosome_index]
    best_value = calculate_fitness(best_chromosome, weights, values, capacity)
    best_weight = 0

    for i in range(len(best_chromosome)):
        if best_chromosome[i] == 1:
            best_weight = best_weight + weights[i]
        
    return best_chromosome, best_weight, best_value




