# Stock Price Prediction for Ford Motors

## Introduction

This project aims to predict the stock prices of Ford Motors using historical data obtained from Yahoo Finance. The dataset spans from January 1, 1972, to February 12, 2024, and includes daily open, high, low, close, adjusted close prices, and trading volume. Time Series Analysis techniques are utilized to analyze the historical stock price data, perform feature engineering, train machine learning models, and predict future stock prices.

## Dataset

The dataset used in this project is obtained from Yahoo Finance and contains historical stock price data for Ford Motors. It includes the following columns:
- Date: The date of the trading day
- Open: The opening price of the stock
- High: The highest price of the stock during the trading day
- Low: The lowest price of the stock during the trading day
- Close: The closing price of the stock
- Adj Close: The adjusted closing price of the stock
- Volume: The trading volume of the stock

## Preprocessing

The dataset undergoes preprocessing to handle missing values, remove duplicates, and ensure consistency in the data format. Additionally, the date column is converted to datetime format, and any outliers or anomalies in the data are addressed.

## Feature Engineering

Feature engineering is performed to extract meaningful features from the dataset that can be used for predicting stock prices. This may include creating lag features, rolling statistics, or technical indicators to capture important patterns and trends in the data.

## Model Evaluation

Several machine learning models are trained and evaluated using the historical stock price data. The models are evaluated based on metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2) to assess their performance in predicting future stock prices.

## Visualization

The results of the stock price prediction models are visualized using various plots and charts. This includes visualizing the predicted vs. actual stock prices over time, exploring feature importance, and analyzing trends and patterns in the data.


## Requirements

To run the project, the following Python libraries are required:
- pandas
- numpy
- matplotlib
- scikit-learn

You can install these libraries using the following command:

```bash
pip install -r requirements.txt
```
## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-price-prediction.git
```
2. Navigate to the project directory:
```bash
cd stock-price-prediction
```
3. Run the Python script `predict_stock_prices.py` using the following command:
```bash
python predict_stock_prices.py
```
## License
This project is licensed under the MIT License. See the [LICENSE]() file for details.















