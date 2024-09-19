# Write a Python script using Matplotlib to create a labeled pie chart representing the profit distribution over the years 2016 to 2020

import matplotlib.pyplot as plt
years = [2016, 2017, 2018, 2019, 2020]
profit = [50000, 80000, 120000, 150000, 180000]
plt.pie(profit, labels=years, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
plt.title('Profit Distribution')
plt.axis('equal')
plt.show()