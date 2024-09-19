# The following Python code uses Matplotlib to create a scatter plot comparing two groups with different income and savings patterns. What will the resulting plot look like when you run the code?

import matplotlib.pyplot as plt
x = [1, 1.5, 2, 2.5, 3, 3.5, 3.6]
y =  [7.5, 8, 8.5, 9, 9.5, 10, 10.5]
x1 = [8, 8.5, 9, 9.5, 10, 10.5, 11]
y1 = [3, 3.5, 3.7, 4, 4.5, 5, 5.2]
plt.scatter(x, y, label='High Income Low Savings', color='r')
plt.scatter(x1, y1, label='Low Income High Savings', color='b')
plt.xlabel('Saving 100')
plt.ylabel('Income 100')
plt.title('Scatter Plot')
plt.legend()
plt.show()