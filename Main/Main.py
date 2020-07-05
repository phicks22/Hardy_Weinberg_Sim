from Model.Population import Population

class Main:

    num_pops = 3
    pop_dict = dict()

    for i in range(num_pops):
        pop_dict[i] = Population(0.7, 0.7, 1.0, 0.9, 10, 20, 0.0, 0.0, 0.0, False)

    for key in pop_dict:
        temp_pop = pop_dict[key].calculate_p_t()
        print(temp_pop)






















# class Main(Population):
#
#     def __init__(self, p, w11, w12, w22, n, gen, u, v, m, inf_pop, num_pop):
#         super().__init__(p, w11, w12, w22, n, gen, u, v, m, inf_pop)
#         self.num_pop = num_pop
#         self.pop_dict = dict()
#
#     def calculate_p_t(self):
#         """Calculates p over t generations implementing fitness, mutation, migration, and drift.
#
#         Arg:
#             None
#
#         Returns:
#             Visualisation of how p changes over t generations for each population
#
#
#         """
#         self.pop_dict.update({'Population': 0})
#         pop_list = []
#         pop_freq = []
#         for i in range(self.num_pop):
#             pop_list.append(Population)
#
#         for object in pop_list:
#             np.char.replace(pop_list, Population, [object])
#
#
#         for generation in range(self.gen):
#             # pop_freq = []
#             for population in pop_list:
#                 population.fitness(self)
#                 population.mutation(self)
#                 population.migration(self)
#                 population.genetic_drift(self)
#                 pop_freq.append(self.p)
#
#
#         print(pop_list)
#         print(pop_freq)
#
#
# # pop = Main(p, w11, w12, w22, n, gen, u, v, m, inf_pop, num_pop)
#
#
# pop = Main(0.8, 0.7, 1.0, 0.8, 100, 10, 0.0, 0.0, 0.0, False, 3)
#
#
# pop.calculate_p_t()
