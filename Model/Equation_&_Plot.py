import math
import matplotlib.pyplot as plt
import numpy as np


class Population:

    def __init__(self):
        self.p = 0.9
        self.q = 0.1
        self.fitness_dict = dict.fromkeys({'w11', 'w12', 'w22'}, 1.0)
        self.npop = 1
        self.generations = 10

    def set_fitness(self):
        w11 = float(input('w11 = '))
        self.fitness_dict['w11'] = w11
        w12 = float(input('w12 = '))
        self.fitness_dict['w12'] = w12
        w22 = float(input('w22 = '))
        self.fitness_dict['w22'] = w22

    def set_parameters(self):
        self.npop = int(input('How many populations? '))
        self.generations = int(input('How many generations? '))
        w11 = float(input('w11 = '))
        self.fitness_dict['w11'] = w11
        w12 = float(input('w12 = '))
        self.fitness_dict['w12'] = w12
        w22 = float(input('w22 = '))
        self.fitness_dict['w22'] = w22



    # def change_fitness(self):
    #     genotype = input('Which genotype? ')
    #     new_value = float(input('What\'s the new fitness coefficient? '))
    #     # print(new_value)
    #     # if 0 <= new_value <= 1:
    #     #     new_value = random.random()
    #     self.fitness_dict[genotype] = new_value

    def freq_equation(self):
        global generations
        generations = int(input('How many generations? '))
        p_over_gen_array = [self.p]
        for gen in range(1, generations):
            w_hat = (self.fitness_dict['w11'] * math.pow(self.p, 2)) + (self.fitness_dict['w12'] * (
                    2 * self.p * self.q)) + (self.fitness_dict['w22'] * math.pow(self.q, 2))
            p_t = ((math.pow(self.p, 2) * self.fitness_dict['w11']) + (self.p * self.q * self.fitness_dict['w12']) /
                   w_hat)
            p_over_gen_array.append(p_t)

            if p_t <= 0:
                break
            self.p = p_t
            self.q = 1 - p_t
            generations = generations
        self.plot(p_over_gen_array)
        print(p_over_gen_array)

    def plot(self, p_over_gen_array):
        t = np.arange(0.0, generations, 1)
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
