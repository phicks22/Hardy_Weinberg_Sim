from Model.Population import Population
from Main.Main import Main
import numpy as np
import matplotlib.pyplot as plt


class Plot:

    def plot(self):
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
