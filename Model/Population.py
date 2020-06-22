import math
import numpy as np


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
        self.q = 1 - self.p
        self.hetero = 2 * self.p * self.q

    def fitness(self):
        """Calculates the frequency of p after selection.

        Args:
            None

        Returns:
            None

        """
        p = self.p
        q = (1 - self.p)

        w_bar = (self.w11 * (p ** 2.0)) + (self.w12 * (2.0 * p * q)) + (self.w22 * (q ** 2.0))
        # p_t = math.sqrt((((self.p ** 2) * self.w11) + (p * q * self.w12) / w_bar))
        p_t = math.sqrt((self.p ** 2) * self.w11 / w_bar)
        q_t = 1 - p_t
        hetero_t = 2 * math.sqrt(p_t) * math.sqrt(q_t)

        self.hetero = hetero_t
        self.p = p_t
        self.q = q_t

        # print(self.p + self.q)
        # print(self.p)
        # print(w_bar)

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
        """Calculates the frequency of p after genetic drift using binomial distribution.

        Args:
            None

        Returns:
            None

        """

        if self.inf_pop is False:

            self.fitness()
            a = np.random.binomial(self.n, self.p, 1)
            num_homo_dom = a[0]
            if self.p < 1:
                b = np.random.binomial((self.n - num_homo_dom), self.p * (1 - self.p), 1)
                num_hetero = b[0]
            else:
                num_hetero = 0

            p = ((2 * num_homo_dom) + num_hetero) / (2 * self.n)

            self.p = p

            return self.p

        else:
            pass


# pop = Population(0.5, 1.0, 1.0, 1.0, 100, 100, 0.0, 0.0, 0.0, False)
# pop.genetic_drift()
