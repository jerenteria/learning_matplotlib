# Import so we dont have to keep typing pyplot repeatedly
import matplotlib.pyplot as plt

# List that will be plotted
squares = [1,4,9,16,25]
# fig = entire figure or collection of plots that are generated, ax = single plot in the figure 
# subplots() can generate one or more plots in the same figure
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

plt.show()