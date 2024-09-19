# Write a Python script using Matplotlib to create a labeled pie chart with an exploded view for 'Product A' and 'Product C', showing the stock distribution of four products: Product A, Product B, Product C, and Product D.

import matplotlib.pyplot as plt
products = ['Product A', 'Product B', 'Product C', 'Product D']
stock = [50, 30, 20, 10]
exploded = [0.1, 0, 0.1, 0] 
plt.pie(stock, labels=products, autopct='%1.1f%%', startangle=140, explode=exploded, wedgeprops={'edgecolor': 'black'})
plt.title('Stock Distribution')
plt.axis('equal')
plt.show()