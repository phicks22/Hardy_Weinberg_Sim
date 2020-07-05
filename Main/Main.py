from Model.Population import Population
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Main:
    num_pops = 5
    pop_dict = dict()

    # Input initial population attributes Population(p, w11, w12, w22, N, generations, u, v, m, infinite pop(bool))
    # Creates dictionary of Population instances
    for i in range(num_pops):
        pop_dict[i] = Population(0.5, 0.4, 0.7, 0.6, 1000, 100, 0.0, 0.0, 0.0, True)

    # Reassigns key values to the list of p frequencies for each Population, [i]
    for key in pop_dict:
        temp_pop = pop_dict[key].calculate_p_t()
        pop_dict[key] = temp_pop

    # Make a data frame
    df = pd.DataFrame({'x': range(0, 101)})

    for key in pop_dict:
        y_values = pop_dict[key]
        df[key] = y_values

    # style
    plt.style.use('seaborn')

    # Color palette
    palette = plt.get_cmap('Set1')

    # Multiple line plot
    num = 0
    for column in df.drop('x', axis=1):
        num += 1
        plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1.25, alpha=0.9, label=column)

    # Titles
    plt.title("Frequency of p", loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Generations")
    plt.ylabel("Frequency")
    plt.ylim(0, 1)
    plt.show()

