from Model.Population import Population
import numpy as np
import matplotlib.pyplot as plt


class Plot(Population):

    def __init__(self, p, w11, w12, w22, n, gen, u, v, m, inf_pop):
        super().__init__(p, w11, w12, w22, n, gen, u, v, m, inf_pop)

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
