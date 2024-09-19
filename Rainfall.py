# Generate the correlations, pairwise relationships, and trends over time for weather data (such as temperature and rainfall) using Python?
# This code performs the following tasks:

# * Loads the weather dataset from a CSV file.
# * Fills missing values with forward fill (ffill).

# * Computes the correlation matrix and visualizes it as a heatmap. 
# * Creates pairwise plots to visualize relationships between different weather variables.

# * Plots the temperature and rainfall trends over time using a dual-axis plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('weather_data.csv')


df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df.ffill(inplace=True)


numeric_df = df.select_dtypes(include=['float64', 'int64'])


corr = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()  
sns.pairplot(numeric_df)
plt.suptitle('Pairwise Relationships', y=1.02)
plt.show() 

fig, ax1 = plt.subplots()

ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color='b')
ax1.plot(df.index, df['Temperature'], color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.set_ylabel('Rainfall (mm)', color='r')
ax2.plot(df.index, df['Rainfall'], color='r')
ax2.tick_params(axis='y', labelcolor='r')


fig.tight_layout()
plt.title('Temperature and Rainfall Trends')
plt.show()  