from Model.Population import Population
import numpy as np
import matplotlib.pyplot as plt


class Main(Population):

    def __init__(self, p, w11, w12, w22, gen, n, u, v, m, inf_pop, num_pop):
        super().__init__(p, w11, w12, w22, gen, n, u, v, m, inf_pop)
        self.num_pop = num_pop
        self.pop_dict = dict()

    def calculate_p_t(self):
        """Calculates p over t generations implementing fitness, mutation, migration, and drift.

        Arg:
            None

        Returns:
            Visualisation of how p changes over t generations for each population


        """
        pop_list = []
        pop_freq = []
        for i in range(self.num_pop):
            pop_list.append(Population)

            # self.pop_dict = defaultdict(list)

        # for item in pop_list:
        #     self.pop_dict[item] = pop_freq
        #     # self.pop_dict[Main].append(item)

        # for key in self.pop_dict:
        # for i in pop_list:
            for generation in range(self.gen):

                for population in pop_list:
                    population.fitness(self)
                    population.mutation(self)
                    population.migration(self)
                    population.genetic_drift(self)
                    pop_freq.append(self.p)

                # self.plot(pop_p)
                # return print(pop_p)
            # self.pop_dict[key].append(pop_list)

        return self.plot(pop_freq)

    def plot(self, pop_freq):
        """Plots frequency of p over x generations for each population.

        Args:
            pop_freq

        Returns:
            None

        """
        t = np.arange(0.0, self.gen, 1)
        s = pop_freq

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlim=(0, self.gen), ylim=(0, 1), xlabel='Generations', ylabel='Frequency',
               title='Frequency p')
        ax.grid()

        plt.show()

# pop = Main(p, w11, w12, w22, gen, n, u, v, m, inf_pop, num_pop)


pop = Main(0.5, 0.7, 1.0, 1.0, 1000, 100, 0.0, 0.0, 0.0, False, 1)


pop.calculate_p_t()
