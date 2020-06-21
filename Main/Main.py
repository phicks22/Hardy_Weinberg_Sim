from Model.Population import Population

# # Input population properties (p, w11, w12, w22, n, gen, u, v, m, inf_pop)
# pop = Population(0.9, 1, 1, 1, 100, 100, 0, 0, 0, True)
# num_pop = 100
#
# # Creates list of populations
# pop_list = []
#
# for population in range(num_pop):
#     pop_list.append(pop)


class Main(Population):

    pop = Population(0.9, 1, 1, 1, 100, 100, 0, 0, 0, True)
    # num_pop = 100
    # pop_list = []
    #
    # for i in range(num_pop):
    #     pop_list.append(pop)

    def __init__(self):

        Population.__init__(self, self.fitness(), self.mutation(), self.migration(), self.genetic_drift())




    def calculate_p_t(self, num_pop):
        """Calculates p over t generations implementing fitness, mutation, migration, and drift.

        Arg:
            None

        Returns:
            Visualisation of how p changes over t generations for each population


        """
        pop = Population(0.9, 1, 1, 1, 100, 100, 0, 0, 0, True)
        num_pop = num_pop
        pop_list = []

        for i in range(num_pop):
            pop_list.append(pop)

        for generation in range(self.gen):
            pop_p = []

            for population in pop_list:
                population.fitness()
                population.mutation()
                population.migration()
                population.genetic_drift()
                pop_p.append(self.p)

        return pop_p

pop.calculate_p_t(3)







# Fitness
# p^2*w11 + 2pq*w12 + q^2*w22 = 1
# p_t = math.sqrt((1 - ((2 * self.q * self.p * (self.fitness_dict['w12']/w_hat)) + (math.pow(self.q, 2)

# Mutation
# p_t+1 = p_t(1-u) + q_t(v)
# u = forward mutation rate
# v = backward mutation rate

# Genetic Drift
# Binomial Distribution -> Pr(k | p, n) = [n! / k! (n - k)!]pk(1-p)n-k
# n! is permutation
# k! (n - k)! is combination -> all possible combinations
# pn(pqn - 1)
# Don't add more variables ->

# * (self.fitness_dict['w22']/w_hat))) / (self.fitness_dict['w11']/w_hat)))

