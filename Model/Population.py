import numpy as np


class Population:

    # You could make default vars in here
    def __init__(self, p=0.5, w11=1.0, w12=1.0, w22=1.0, n=100, gen=400, u=0.0, v=0.0, m=0.0, inf_pop=False):
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
        self.population_frequency_list = list()

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
        p_t = ((p ** 2) * self.w11) / w_bar
        q_t = 1 - p_t
        hetero_t = (2 * p * q * self.w12) / w_bar

        self.hetero = hetero_t
        self.p = p_t
        self.q = q_t

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

            a = np.random.binomial(self.n, self.p, 1)
            num_homo_dom = a[0]
            if self.p < 1:
                b = np.random.binomial((self.n - num_homo_dom), self.hetero / (1 - self.p), 1)
                num_hetero = b[0]
            else:
                num_hetero = 0

            self.p = ((2 * num_homo_dom) + num_hetero) / (2 * self.n)

            return self.p

        else:
            pass

    def calculate_p_t(self):
        """Calculates p over t generations implementing fitness, mutation, migration, and drift.

        Arg:
            None

        Returns:
            Visualisation of how p changes over t generations for each population


        """
        self.population_frequency_list = [self.p]

        for gen in range(self.gen):
            self.mutation()
            self.migration()
            self.fitness()
            self.genetic_drift()
            self.population_frequency_list.append(self.p)
