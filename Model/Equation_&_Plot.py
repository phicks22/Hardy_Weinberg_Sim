import math
import matplotlib.pyplot as plt
import numpy as np


class Population:

    def __init__(self, p, npop, gen, u, v):
        self.p = p
        self.fitness_dict = dict.fromkeys({'w11', 'w12', 'w22'}, 1.0)
        self.npop = npop
        self.gen = gen
        self.u = u
        self.v = v

    def set_fitness(self):
        w11 = float(input('w11 = '))
        self.fitness_dict['w11'] = w11
        w12 = float(input('w12 = '))
        self.fitness_dict['w12'] = w12
        w22 = float(input('w22 = '))
        self.fitness_dict['w22'] = w22

    def set_parameters(self):
        self.npop = int(input('Populations = '))
        self.gen = int(input('Generations = '))
        w11 = float(input('w11 = '))
        self.fitness_dict['w11'] = w11
        w12 = float(input('w12 = '))
        self.fitness_dict['w12'] = w12
        w22 = float(input('w22 = '))
        self.fitness_dict['w22'] = w22
        self.u = float(input('Forward mutation frequency = '))
        self.v = float(input('Backward mutation frequency = '))

    # def change_fitness(self):
    #     genotype = input('Which genotype? ')
    #     new_value = float(input('What\'s the new fitness coefficient? '))
    #     # print(new_value)
    #     # if 0 <= new_value <= 1:
    #     #     new_value = random.random()
    #     self.fitness_dict[genotype] = new_value

    def freq_equation(self):
        global gen
        gen = self.gen
        p_over_gen_array = [self.p]
        for g in range(1, gen):
            w_hat = (self.fitness_dict['w11'] * math.pow(self.p, 2)) + (self.fitness_dict['w12'] * (
                    2 * self.p * (1 - self.p))) + (self.fitness_dict['w22'] * math.pow((1 - self.p), 2))
            p_t = ((math.pow(self.p, 2) * self.fitness_dict['w11']) + (self.p * (1 - self.p) * self.fitness_dict['w12'])
                   / w_hat)
            p_over_gen_array.append(p_t)

            if p_t <= 0:
                break
            self.p = p_t
            gen = gen
        self.plot(p_over_gen_array)
        print(p_over_gen_array)

    def plot(self, p_over_gen_array):
        t = np.arange(0.0, gen, 1)
        s = p_over_gen_array

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='Generations', ylabel='Frequency',
               title='p')
        ax.grid()

        plt.show()


pop1 = Population()

pop1.set_fitness()
pop1.freq_equation()

# Fitness
# p^2*w11 + 2pq*w12 + q^2*w22 = 1
# p_t = math.sqrt((1 - ((2 * self.q * self.p * (self.fitness_dict['w12']/w_hat)) + (math.pow(self.q, 2)

# Mutation
# p_t+1 = p_t(1-u) + q_t(v)
# u = forward mutation rate
# v = backward mutation rate

# * (self.fitness_dict['w22']/w_hat))) / (self.fitness_dict['w11']/w_hat)))
