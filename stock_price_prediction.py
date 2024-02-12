# -*- coding: utf-8 -*-
"""stock-price-prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17kfL2LAjYi5SHvxKE0vKKlSN2R830JJS
"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('/content/F.csv')

# Convert the date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the date column as the index
data.set_index('Date', inplace=True)

# Visualize the closing price
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Feature engineering
data['Day'] = data.index.day
data['Month'] = data.index.month
data['Year'] = data.index.year

# Define features and target variable
X = data[['Day', 'Month', 'Year']]
y = data['Close']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Visualize the predicted vs. actual prices
plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test.values, label='Actual Price')
plt.plot(y_test.index, y_pred, label='Predicted Price')
plt.title('Predicted vs. Actual Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()