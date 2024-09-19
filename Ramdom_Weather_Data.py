# Generate random weather data (temperature, humidity, wind speed, and rainfall) for each day of the year 2023 and save it to a CSV file using Python?

import numpy as np
import pandas as pd
data_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
np.random.seed(0)
temperature = np.random.normal(loc = 10, scale=5, size=len(data_range))
humidity = np.random.uniform(60, 90, size=len(data_range))
wind_speed = np.random.uniform(5, 20, size=len(data_range))
rainfall = np.random.exponential(scale=2, size=len(data_range))
df = pd.DataFrame({'Date': data_range, 'Temperature': temperature, 'Humidity': humidity, 'Wind Speed': wind_speed, 'Rainfall': rainfall})
df.to_csv('weather_data.csv', index=False)
print("Weather data has been saved to 'weather_data.csv'")