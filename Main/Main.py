from Model.Population import Population
import matplotlib.pyplot as plt
import numpy as np


class Main:
    num_pops = 5
    pop_dict = dict()
    num_gen = 0
    x_values = []
    index = 0

    # Input initial population attributes Population(p, w11, w12, w22, N, generations, u, v, m, infinite pop(bool))
    # Creates dictionary of Population instances
    for i in range(num_pops):
        pop_dict[i] = Population()

    # style
    plt.style.use('seaborn')

    # Color palette
    palette = plt.get_cmap('Set1')

    # Reassigns key values to the list of p frequencies for each Population, [i]
    for key in pop_dict:
        if key == 0:
            num_gen = pop_dict[key].gen
            x_values = np.arange(0, num_gen + 1)

        pop_dict[key].calculate_p_t()
        plt.plot(x_values, pop_dict.get(key).population_frequency_list, marker='', color=palette(index), linewidth=1.25,
                 alpha=0.9)
        index += 1

    # Titles
    plt.title("Frequency of p", loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Generations")
    plt.ylabel("Frequency")
    plt.ylim(0, 1)
    plt.show()
