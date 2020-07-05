from Model.Population import Population
from Main.Main import Main
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make a data frame
df = pd.DataFrame({'x': range(1, 11), 'y1': np.random.randn(10), 'y2': np.random.randn(10) + range(1, 11),
                   'y3': np.random.randn(10) + range(11, 21), 'y4': np.random.randn(10) + range(6, 16),
                   'y5': np.random.randn(10) + range(4, 14) + (0, 0, 0, 0, 0, 0, 0, -3, -8, -6),
                   'y6': np.random.randn(10) + range(2, 12), 'y7': np.random.randn(10) + range(5, 15),
                   'y8': np.random.randn(10) + range(4, 14), 'y9': np.random.randn(10) + range(4, 14),
                   'y10': np.random.randn(10) + range(2, 12)})

# style
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

# multiple line plot
num = 0
for column in df.drop('x', axis=1):
    num += 1
plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)

# Add legend
plt.legend(loc=2, ncol=2)

# Add titles
plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Score")

plt.show()


# class Plot:
#
#     def plot(self):
#         """Plots frequency of p over x generations for each population.
#
#         Args:
#             pop_freq
#
#         Returns:
#             None
#
#         """
#         t = np.arange(0.0, self.gen, 1)
#         s = pop_freq
#
#         fig, ax = plt.subplots()
#         ax.plot(t, s)
#
#         ax.set(xlim=(0, self.gen), ylim=(0, 1), xlabel='Generations', ylabel='Frequency',
#                title='Frequency p')
#         ax.grid()
#
#         plt.show()

