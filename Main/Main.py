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
        # # because i Defended default vars you dont have to write this
        # pop_dict[i] = Population(0.5, 1.0, 0.3, 1.0, 1000, 100, 0.0, 0.0, 0.0, False)

        # this is equivalent now
        pop_dict[i] = Population()

        # # if you want to adjust var you just do
        # pop_dict[i] = Population(w11= 1.3, w22=3.5)

    # style
    plt.style.use('seaborn')

    # Color palette
    palette = plt.get_cmap('Set1')

    # Reassigns key values to the list of p frequencies for each Population, [i]
    for key in pop_dict:
        # # i made it shorter. Left side always will be executed first

        # # instead of making another loop you can plot it in this one and just call function show later on
        # # if i am looping through this dict for the fist time i check how many generations there is and adjust plot

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
