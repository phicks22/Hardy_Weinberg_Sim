from Model.Population import Population
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


class Main(Population):

    # pop = Population(0.9, 1, 1, 1, 100, 100, 0, 0, 0, True)
    # # num_pop = 100
    # # pop_list = []
    # #
    # # for i in range(num_pop):
    # #     pop_list.append(pop)

    num_pop = None

    def __init__(self, p, w11, w12, w22, gen, n, u, v, m, inf_pop, num_pop):
        super().__init__(p, w11, w12, w22, gen, n, u, v, m, inf_pop)
        self.num_pop = num_pop
        self.pop_list = []

    def calculate_p_t(self):
        """Calculates p over t generations implementing fitness, mutation, migration, and drift.

        Arg:
            None

        Returns:
            Visualisation of how p changes over t generations for each population


        """
        # pop = Population(0.9, 1, 1, 1, 100, 100, 0, 0, 0, True)
        # num_pop = num_pop
        # pop_list = []

        for i in range(self.num_pop):
            self.pop_list.append(Population)

        for generation in range(self.gen):
            pop_p = []

            for population in self.pop_list:
                population.fitness(self)
                population.mutation(self)
                population.migration(self)
                population.genetic_drift(self)
                pop_p.append(self.p)

            # self.plot(pop_p)
            return print(pop_p)

    def plot(self, pop_p):
        t = np.arange(0.0, self.gen, 1)
        s = pop_p

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='Generations', ylabel='Frequency',
               title='p')
        ax.grid()

        plt.show()

# pop = Main(p, w11, w12, w22, gen, n, u, v, m, inf_pop, num_pop)


pop = Main(0.9, 1.0, 1.0, 1.0, 100, 100, 0.0, 0.0, 0.0, False, 3)


pop.calculate_p_t()
