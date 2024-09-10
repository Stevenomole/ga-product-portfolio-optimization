# imports
from genetic_algorithm import GeneticAlgorithm
from data_processing import load_data, preprocess_data
import os

# Global variables to store preprocessed data
module_profile = None
dependencies = {}
feasible_set = {}

def preprocess_data_once():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'Data', 'data_bank.xlsx')
    
    cost_profile_inh, resource_util_inh, resource_avail_inh, crash_data_inh, crash_data_out, preced = load_data(file_path)
    return preprocess_data(cost_profile_inh, resource_util_inh, resource_avail_inh, crash_data_inh, crash_data_out, preced)

def run_genetic_algorithm(input_params):
    module_profile, dependencies, feasible_set = preprocess_data_once()

    ga = GeneticAlgorithm(module_profile, dependencies, feasible_set, None, None)
    population_size = int(input_params['population'])
    mutation_rate = float(input_params['mutationRate'])
    crossover_rate = float(input_params['crossoverRate'])
    generations = int(input_params['generations'])
    interaction_degree = input_params['interactionMatrix']
    information_flow = input_params['informationMatrix']
    adoption_rate = input_params['adoptionRate']

    ga.interaction_degree = interaction_degree
    ga.information_flow = information_flow

    # Run the update_module_duration function
    ga.update_module_duration()
    print("Updated module durations:")

    best_solution, best_fitness, best_product_selection = ga.run(population_size, crossover_rate, mutation_rate, generations)

    return {
        "best_solution": best_solution,
        "fitness": best_fitness,
        "product_selection": best_product_selection
    }

'''
# Example usage
if __name__ == "__main__":
    input_params = {
        "population": 100,
        "mutation_rate": 0.1,
        "crossover_rate": 0.5,
        "generations": 10,
        "interaction_degree": 20,
    }
    result = run_genetic_algorithm(input_params)
    print(f"Best fitness: {result['fitness']}")
    print(f"Best solution: {result['best_solution']}")
'''
