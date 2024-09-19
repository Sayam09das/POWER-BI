# Create a plot using Matplolib and python where time spent on activits(sleeping,eating,working,playing) over & days.Take the Values as you want, What will the resulting plot look like when you run the code ?
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sleeping = [7, 8, 7, 8, 6, 10, 12]
eating = [2, 3, 2, 1, 2, 3, 3]
working = [8, 7.5, 8, 8.5, 8, 2, 0]
playing = [3, 4, 3, 2, 4, 7, 12]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
plt.xlabel('Days')
plt.ylabel('Time')
plt.title('Activity Distribution')
plt.legend()
plt.show()