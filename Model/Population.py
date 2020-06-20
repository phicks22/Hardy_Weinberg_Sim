class Population:

    def __init__(self, p, w11, w12, w22, n, gen, u, v, inf_pop):
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
        self.inf_pop = inf_pop