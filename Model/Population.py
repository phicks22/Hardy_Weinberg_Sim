import math
import matplotlib.pyplot as plt
import numpy as np
import random


class Population:

    def __init__(self, p, w11, w12, w22, n, gen, u, v, m, inf_pop):
        """ Population class for setting a population to calculate object attributes after
         the number of generations given.

         Attributes:
             p (float) representing allele frequency
                - q is (1-p)
             w11 (float) representing the P fitness coefficient
             w12 (float) representing the 2pq fitness coefficient
             w22 (float) representing the Q fitness coefficient
             n (int) representing the population size
             gen (int) number of generations the simulation will iterate through
             u (float) representing the forward mutation rate
             v (float) representing the backward mutation rate
             m (float) representing the migration rate of the populations
             inf_pop (bool) identifies if a population will experience genetic drift (False) or not (True)
         """
        self.p = p
        self.w11 = w11
        self.w12 = w12
        self.w22 = w22
        self.n = n
        self.gen = gen
        self.u = u
        self.v = v
        self.m = m
        self.inf_pop = inf_pop

    def fitness(self):
        """Calculates the frequency of p after selection.

        Args:
            None

        Returns:
            None

        """
        w_bar = (self.w11 * (self.p ** 2.0)) + (self.w12 * (2.0 * self.p * (1.0 - self.p))) + (
                    self.w22 * ((1.0 - self.p) ** 2.0))
        p_t = (((self.p ** 2) * self.w11) + (self.p * (1 - self.p) * self.w12) / w_bar)
        self.p = p_t

    def mutation(self):
        """Calculates the frequency of p after mutation.

        Args:
            None

        Returns:
            None

        """

        p_t = (self.p * (1.0 - self.u)) + ((1.0 - self.p) * self.v)
        self.p = p_t

    def migration(self):
        """Calculates the frequency of p after migration

        Args:
            None

        Returns:
            None

        """

        pass

    # TODO figure out how to do migration

    def genetic_drift(self):
        """Calculates the frequency of p after genetic drift using a binomial distribution.

        Args:
            None

        Returns:
            None

        """

        if self.inf_pop is False:
            arr = []
            for gen in range(self.gen):
                a = ((math.factorial(2 * self.n)) / ((math.factorial(2 * self.n * round(self.p))) * (math.factorial((2 * self.n) - (2 * self.n * round(self.p))))))
                b = (math.pow(self.p, (2 * self.n * self.p))) * (math.pow((1 - self.p), (2 * self.n) - (2 * self.n * self.p)))
                prob_unchanged = a * b
                if prob_unchanged < 0.5:
                    self.p = random.uniform(0, 1)
                    arr.append(self.p)
                else:
                    arr.append(self.p)

            return print(arr)

        else:
            pass


pop = Population(0.9, 0.8, 1.0, 1.0, 10, 100, 0.0, 0.0, 0.0, False)
pop.genetic_drift()
