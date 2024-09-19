# Create a box plot using Matplotlib for two datasets. Take the values as you want. What will the resulting plot look like when you run the code?
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [10, 20, 40, 5, 30, 60, 90]
Z = [X,Y]
plt.boxplot(Z, label= ["A", "B"], showmeans= True)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()