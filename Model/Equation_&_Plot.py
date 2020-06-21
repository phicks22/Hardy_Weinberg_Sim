# import math
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# class Population:
#
#     def __init__(self):
#         self.p = 0.0
#         self.fitness_dict = dict.fromkeys({'w11', 'w12', 'w22'}, 1.0)
#         self.npop = 0
#         self.generations = 0
#         self.u = 0.0
#         self.v = 0.0
#         self.inf_pop = False
#         self.pop_size = 0
#
#     def set_fitness(self):
#         w11 = float(input('w11 = '))
#         self.fitness_dict['w11'] = w11
#         w12 = float(input('w12 = '))
#         self.fitness_dict['w12'] = w12
#         w22 = float(input('w22 = '))
#         self.fitness_dict['w22'] = w22
#
#     def set_parameters(self):
#         self.p = float(input('Frequency p = '))
#         self.npop = int(input('Populations = '))
#         self.generations = int(input('Generations = '))
#         w11 = float(input('w11 = '))
#         self.fitness_dict['w11'] = w11
#         w12 = float(input('w12 = '))
#         self.fitness_dict['w12'] = w12
#         w22 = float(input('w22 = '))
#         self.fitness_dict['w22'] = w22
#         self.u = float(input('Forward mutation frequency = '))
#         self.v = float(input('Backward mutation frequency = '))
#         self.inf_pop = bool(input('Infinite population = '))
#         self.pop_size = int(input('Population size = '))
#
#     # def change_fitness(self):
#     #     genotype = input('Which genotype? ')
#     #     new_value = float(input('What\'s the new fitness coefficient? '))
#     #     # print(new_value)
#     #     # if 0 <= new_value <= 1:
#     #     #     new_value = random.random()
#     #     self.fitness_dict[genotype] = new_value
#
#     def freq_equation(self):
#         global generations, npop, p_tf
#         generations = self.generations
#         npop = self.npop
#         u = float(self.u)
#         v = float(self.v)
#         for p in range(0, npop):
#             p_over_gen_array = [self.p]
#             for g in range(1, generations):
#
#                 # fitness
#                 w_hat = (self.fitness_dict['w11'] * math.pow(self.p, 2)) + (self.fitness_dict['w12'] * (
#                         2 * self.p * (1 - self.p))) + (self.fitness_dict['w22'] * math.pow((1 - self.p), 2))
#                 p_t = ((math.pow(self.p, 2) * self.fitness_dict['w11']) + (
#                             self.p * (1 - self.p) * self.fitness_dict['w12'])
#                        / w_hat)
#                 hetero = (2 * self.p * (1 - self.p) * self.fitness_dict['w12']) / w_hat
#
#                 # mutation
#                 if self.u or self.v > 0.0:
#                     p_tf = p_t * (1.0 - u) + (1.0 - p_t) * v
#                     p_over_gen_array.append(p_tf)
#                 else:
#                     p_tf = p_t
#                     p_over_gen_array.append(p_tf)
#
#                 if self.inf_pop == False:
#                     tpr = ((math.factorial(2 * npop)) / ((math.factorial(2 * npop * p_tf)) * (math.factorial((2*npop) -
#                             (2 * npop * p_tf))))) * (math.pow(p_tf, (2 * npop * p_tf))) * (math.pow((1 - p_tf), (2 * npop) -
#                             (2 * npop * p_tf)))
#                     # np_t = np.random.binomial(1, p_t, self.pop_size)
#
#                 elif self.inf_pop == True:
#                     p_tf = p_tf
#
#                 if p_tf <= 0:
#                     break
#                 self.p = p_tf
#                 generations = generations
#                 npop = npop
#             self.plot(p_over_gen_array)
#             print(p_over_gen_array)
#
#     # TODO: plot both populations on same graph
#     # TODO: make list for freq_p of each population and run separate loop for each
#     # TODO: Incorporate binomial distribution and genetic drift for population
#
#     def plot(self, p_over_gen_array):
#         t = np.arange(0.0, generations, 1)
#         s = p_over_gen_array
#
#         fig, ax = plt.subplots()
#         ax.plot(t, s)
#
#         ax.set(xlabel='Generations', ylabel='Frequency',
#                title='p')
#         ax.grid()
#
#         plt.show()
#
#
# pop1 = Population()
#
# pop1.set_parameters()
# pop1.freq_equation()

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
