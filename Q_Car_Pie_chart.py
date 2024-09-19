# Write a Python script using Matplotlib to create a labeled pie chart showing the sales distribution of Audi, BMW, Ford, Tesla, Jaguar, and Mer

import matplotlib.pyplot as plt
Car = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERECDES']
DATA = [23, 17, 35, 29, 12, 41]
plt.pie(DATA, labels=Car, autopct='%1.1f%%', startangle=140, wedgeprops= {'edgecolor': 'black'})
plt.title('Sales Distribution')
plt.show()