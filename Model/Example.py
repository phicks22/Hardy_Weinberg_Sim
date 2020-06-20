import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In this script, we will simulate genetic drift in a population with a finite
# size. We'll do this using some random number generation functions within
# Python to watch how the frequency of an allele changes with the nubmer of
# generations. We'll start by defining some parameters.
p = 0.5  # Initial frequency of allele A
N = 50  # Number of (haploid) individuals in the population.
num_gen = 100  # Number of generations to run the simulation.

# We'll start by just looking at single population. To simulate the drift, we
# will flip a coin for each individual and determine if they will get an A or
# a B allele. We can then easily calculate the allele frequency.

# We'll make an empty list to store the frequencies.
freq_a = []
for i in range(num_gen):

    # Now we can flip the coins. We'll flip all of them at once.
    draw = np.random.rand(N)

    # We can determine the number of individuals who get allele A.
    num_a = np.sum((draw < p))

    # Compute the frequency and store it.
    freq = np.sum(num_a) / N
    freq_a.append(freq)
    p = freq

# Now we can plot the allele frequency as a function of time.
gen_vec = np.arange(0, len(freq_a), 1)
plt.figure()
plt.plot(gen_vec, freq_a)
plt.show()

# Everytime you run this script, you'll get a different answer! You can see
# that the time of fixation (when the allele frequency reaches either 1 or 0)
# scales approximately with the number of individuals in the population.

# Let's run this a bunch of times and look at many trajectories at once. To
# do this, we'll do what we just did in a loop and then plot each one as we
# go along.k
plt.figure()
num_simulations = 10

# Do this many times by looping through simulations.
for j in range(num_simulations):
    p = 0.5  # Reset the probability each simulation.
    freq_a = []  # Make an empty storage list.
    for i in range(num_gen):
        # We should really only do this until we reach fixation. We can do this
        # By forcing the loop to only fire if the probability is between 0 and
        # 1.0
        if (p < 1.0) and (p > 0):

            # Flip the coins.
            draw = np.random.rand(N)

            # Count the number of A alleles
            num_a = (draw < p)

            # Compute the frequencies
            freq = np.sum(num_a) / len(num_a)
            freq_a.append(freq)

            # Reset the frequency.
            p = freq

    # Now we'll plot it for each simulation.
    gen_vec = np.arange(0, len(freq_a), 1)
    plt.plot(gen_vec, freq_a)

plt.xlabel('number of generations')
plt.ylabel('allele A frequency')
plt.show()

# You can see that it is very random, yet the alleles will almost always reach
# fixation. To prove that, we'll run this simulation over and over again,
# compute the mean time to fixation, and plot it as a function of population
# size.
# Set up an empty list where we will keep the mean fixation times.
mean_fixation_time = []

# We'll vary the population size
population = [2, 40, 60, 80, 100, 120, 200]

# We'll run eerything one hundred times.
num_simulations = 100

# Now we just loop through and do everything again.
for N in population:
    fixation_time = []
    for i in range(num_simulations):
        p = 0.5
        time = 0
        while (p < 1.0) & (p > 0):
            draw = np.random.rand(N)
            num_a = (draw < p)
            # Count how many a's.
            p = np.sum(num_a) / len(num_a)
            time += 1
        fixation_time.append(time)

    # Now we just have to compute the mean time it took to reach fixation.
    mean_time = np.mean(fixation_time)
    mean_fixation_time.append(mean_time)

# Let's plot it!
plt.figure()
plt.plot(population, mean_fixation_time, 'o')
plt.xlabel('size of population')
plt.ylabel('time to fixation (generations)')
plt.show()

# Now we can see that the time it will take for a specific allele to reach
# fixation scales linearly with the size of the population. I urge you to take
# this code and attempt to include some parameters such as selection and
# mutation.
