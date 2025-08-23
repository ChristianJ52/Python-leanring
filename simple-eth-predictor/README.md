# Simple ETH Price Predictor (Day 6)

A small project that predicts **tomorrow’s ETH/USDT close** using daily data from the public Binance API. Focus: clean data → simple features → time-ordered split → honest baseline.

---

## What it does
- Downloads ~365 daily ETH/USDT candles.
- Builds a small set of explainable features.
- Trains a standardized Linear Regression.
- Compares against a naive baseline (tomorrow = today).
- Plots actual vs predicted.
- Prints a 1-day-ahead forecast.

Run

Run the script: python Ethereum Price Prediction model.py

You’ll see:

- Train/Test date ranges
- RMSE/MAE and naive baseline comparison
- A line chart (actual vs predicted)
- A one-day-ahead forecast number

- ETH/USDT — Actual vs Predicted (1-Day Ahead)
- <img width="1202" height="574" alt="image" src="https://github.com/user-attachments/assets/1365200f-9363-4312-8dcc-b026e3a10bbf" />

Description: Time-series chart showing 1-day-ahead predictions versus actual closing prices. Blue/orange lines are the training period and green/red lines are the test period. The dashed vertical line marks the start of the test window, showing a time-ordered split.#

1) Fetching real data from Binance

<img width="1036" height="554" alt="image" src="https://github.com/user-attachments/assets/b3813d61-dfae-4f66-912e-374d5612be6c" />

What’s happening: I call Binance’s public klines endpoint, parse the JSON into a DataFrame, convert strings to numbers, convert the millisecond timestamp to a UTC DatetimeIndex, and keep only price (close) and volume.
Why it matters: Clean, time-indexed data is needed for any time-series model.

2) Train/Test Split, Pipeline, and Baseline (in train_and_evaluate)

<img width="976" height="761" alt="image" src="https://github.com/user-attachments/assets/ce786bac-2ca7-461d-acd7-dbfa5a29c2df" />

Description: This block does a forward, time-ordered split (no shuffling) to avoid data leakage, builds a pipeline with StandardScaler → LinearRegression, and makes predictions on train and test. It then computes RMSE/MAE, an honest naïve baseline (“tomorrow = today”), the RMSE lift vs that baseline, and directional accuracy (did we get up/down right).

-Glossary
Candle / Kline — One time interval’s market record (Open, High, Low, Close, Volume).

JSON — A simple text format APIs use to send data (lists/objects).

DataFrame (pandas) — A table-like data structure for rows and columns.

Data leakage — When future information sneaks into training and inflates results.

Standardization — Rescaling features to mean 0 and std 1 (z-score scaling).

Pipeline — A chained process (here: StandardScaler → LinearRegression).

Linear Regression — A simple model that learns coefficients to predict a number.

Naïve baseline — A yardstick prediction; here “tomorrow = today.”

RMSE (Root Mean Squared Error) — Average error size with big mistakes penalized more; same units as price.

MAE (Mean Absolute Error) — Average absolute error; easier to interpret, less harsh on outliers.

RMSE lift — Baseline RMSE minus model RMSE; positive means the model beats the baseline.

Moving average (MA) — Average price over the last k days (e.g., MA7 = 7-day average).

Lag / Shift — Using previous values (e.g., lag-1 = yesterday); shift(-1) is tomorrow.

Rolling window — A sliding window over recent data to compute stats repeatedly.

NaN — “Not a Number”; a missing value that appears after rolling/shift operations.
