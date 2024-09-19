# Create a bar Chart using Matplotlib and python that compares the distances travelled by BMW and AUDI cars over several days. Take the values as you want. What will the resulting plot look like when you run the code?

import matplotlib.pyplot as plt
plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20], label='BMW', width=0.5, color= "b")
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60], label='AUDI', width=0.5, color= "r")
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (km)')
plt.title('Distance Comparison')
plt.show()