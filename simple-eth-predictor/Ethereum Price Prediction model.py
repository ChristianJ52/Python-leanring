# Day 6: ETH Price Predictor 
# What I'm practicing today:
#  - Pull ETH/USDT daily data from a public API (Binance)
#  - Build a SMALL set of features I understand
#  - Time-ordered train/test split (no shuffling)
#  - Compare my model to a naive baseline (tomorrow = today)
#  - Make a single 1-day-ahead forecast
#  - One clear plot so I can see what's going on

import math                              # math.sqrt for RMSE and other math utilities
import requests                          # to call the Binance REST API over HTTP
import numpy as np                       # numerical tools (arrays, simple stats)
import pandas as pd                      # to store and transform table-like data
import matplotlib.pyplot as plt          # to make the line chart

from sklearn.pipeline import make_pipeline          # to chain preprocessing + model
from sklearn.preprocessing import StandardScaler    # to standardize features (mean 0, std 1)
from sklearn.linear_model import LinearRegression   # simple linear model for regression
from sklearn.metrics import mean_squared_error, mean_absolute_error  # evaluation metrics

import warnings                          # to control warning messages
warnings.filterwarnings("ignore")        # hide warnings so the console output stays clean


# -----------------------------
# 1) Data: fetch ETH/USDT daily from Binance
# -----------------------------
def fetch_eth_daily(days=365, symbol="ETHUSDT"):     # define a function with defaults: 365 days, ETH/USDT pair
    """
    Grab daily OHLCV candles from Binance's public endpoint.
    I only keep 'close' (as price) and 'volume' to keep this beginner-friendly.
    """
    print("Fetching daily ETH/USDT candles from Binance...")  

    url = "https://api.binance.com/api/v3/klines"   # Binance spot market klines endpoint
    params = {                                      # query parameters for the request
        "symbol": symbol.upper(),                   # the trading pair, uppercase just in case
        "interval": "1d",                           # 1 day candles
        "limit": int(min(max(days, 2), 1000))       # number of rows: between 2 and 1000
    }
    headers = {"User-Agent": "Day6-ETH-Predictor/1.0 (learning project)"}  

    r = requests.get(url, params=params, headers=headers, timeout=20)  # make the HTTP GET request
    r.raise_for_status()                                   # if HTTP status is not OK, raise an error
    raw = r.json()                                         # parse the response as JSON 

    cols = [                                               # names for the columns Binance returns
        "open_time","open","high","low","close","volume","close_time",
        "quote_asset_volume","num_trades","taker_buy_base","taker_buy_quote","ignore"
    ]
    df = pd.DataFrame(raw, columns=cols)                   # build a pandas DataFrame with those names

    # convert number-like strings to floats (Binance sends numbers as strings)
    for c in ["open","high","low","close","volume","quote_asset_volume","taker_buy_base","taker_buy_quote"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")      # convert; non-numeric becomes NaN

    # use close_time (ms) as the daily timestamp and convert to timezone-aware UTC datetime
    df["date"] = pd.to_datetime(df["close_time"], unit="ms", utc=True)
    df.set_index("date", inplace=True)                     # make the datetime the index for time-series ops

    # keep only what I need for a first model: closing price and volume
    df = df[["close","volume"]].rename(columns={"close":"price"})
    df.index.name = "date"                                 

    print(f"Got {len(df)} rows. Range: {df.index.min().date()} → {df.index.max().date()}")  # summary
    print(f"Price range: ${df['price'].min():.2f} to ${df['price'].max():.2f}")             # more info
    return df                                              # hand back the tidy DataFrame


# -----------------------------
# 2) Features: keep them small and sensible
# -----------------------------
def build_features(df):                                    # function to create inputs (X) and target (y)
    """
    Small feature set I can explain:
      - lag_1: yesterday's price (strong simple signal)
      - ma7: 7-day moving average (short trend)
      - price_vs_ma7: how stretched we are vs MA7 (scale-free)
      - ret_1d: 1-day percent change (returns are how markets talk)
      - vol_7d: 7-day std of returns (recent "jumpiness")
      - volume_ratio: today's volume vs 7-day avg (activity spike or not)
    Target:
      - target = tomorrow's price (price shifted -1)
    """
    print("Building features")

    data = df.copy()                                      # work on a copy so original df stays clean

    data["lag_1"] = data["price"].shift(1)               # yesterday’s price
    data["ma7"] = data["price"].rolling(7).mean()        # 7-day moving average of price
    data["price_vs_ma7"] = data["price"] / data["ma7"]   # ratio: current price vs MA7

    data["ret_1d"] = data["price"].pct_change()          # daily return (percent change)
    data["vol_7d"] = data["ret_1d"].rolling(7).std()     # volatility: std of returns over 7 days

    data["vol_avg_7"] = data["volume"].rolling(7).mean() # average volume across last 7 days
    data["volume_ratio"] = data["volume"] / data["vol_avg_7"]  # today’s volume vs that average

    data["target"] = data["price"].shift(-1)             # tomorrow’s price (what we want to predict)

    data = data.dropna()                                  # drop rows with NaNs from rolling/shift

    features = ["lag_1","ma7","price_vs_ma7","ret_1d","vol_7d","volume_ratio"]  # columns to use as X
    X = data[features]                                    # feature matrix
    y = data["target"]                                    # target vector

    print(f"Feature matrix: {X.shape[0]} rows x {X.shape[1]} cols")  # quick shape check
    return X, y, data.index                               # return X, y, and aligned date index


# -----------------------------
# 3) Train/evaluate with a forward split and a naïve baseline
# -----------------------------
def train_and_evaluate(X, y, dates, train_ratio=0.8):     # function to train and score the model
    """
    Time-ordered split (first part train, last part test).
    Model: StandardScaler + LinearRegression (simple and fair).
    I also report a naïve baseline: tomorrow = today.
    """
    print("Training model...")

    n = len(X)                                            # number of rows
    split = int(n * train_ratio)                          # index where train ends and test begins

    X_train, X_test = X.iloc[:split], X.iloc[split:]      # earlier rows for training, later for test
    y_train, y_test = y.iloc[:split], y.iloc[split:]      # same split for target

    # dates is a DatetimeIndex; use direct positional indexing (no .iloc on an index)
    train_start, train_end = dates[0], dates[split - 1]   # first and last train dates
    test_start,  test_end  = dates[split], dates[-1]      # first and last test dates
    print(f"Train window: {train_start.date()} → {train_end.date()}")  # print readable range
    print(f" Test window: {test_start.date()} → {test_end.date()}")

    model = make_pipeline(StandardScaler(), LinearRegression())  # scale features → linear regression
    model.fit(X_train, y_train)                                  # learn the coefficients

    yhat_train = model.predict(X_train)                          # predictions on training data
    yhat_test  = model.predict(X_test)                           # predictions on test data

    # compute core metrics
    train_rmse = math.sqrt(mean_squared_error(y_train, yhat_train))  # RMSE train
    test_rmse  = math.sqrt(mean_squared_error(y_test,  yhat_test))    # RMSE test
    test_mae   = mean_absolute_error(y_test, yhat_test)               # MAE test

    # naïve baseline: predict tomorrow as today for the test set (shift actuals back one)
    naive = y_test.shift(1).bfill().values                       # baseline predictions
    naive_rmse = math.sqrt(mean_squared_error(y_test, naive))     # RMSE of baseline
    rmse_lift  = naive_rmse - test_rmse                           # positive = our model beats baseline

    # directional accuracy: did we at least get up/down correct vs today’s price?
    todays_price = y_test.shift(1).bfill().values                 # “today” aligned to each “tomorrow”
    actual_up = (y_test.values > todays_price)                    # True/False for actual up move
    pred_up   = (yhat_test > todays_price)                        # True/False for predicted up move
    dir_acc   = np.mean(actual_up == pred_up) * 100.0             # percent correct

    # print an easy-to-read summary
    print(f"Training RMSE: ${train_rmse:.2f}")
    print(f"    Test RMSE: ${test_rmse:.2f}")
    print(f"     Test MAE: ${test_mae:.2f}")
    print(f"   Naïve RMSE: ${naive_rmse:.2f}  |  Lift vs naïve: ${rmse_lift:.2f}")
    print(f"Direction accuracy (test): {dir_acc:.1f}%")

    return {                                             # return everything the rest of the script needs
        "model": model,
        "y_train": y_train, "y_test": y_test,
        "yhat_train": yhat_train, "yhat_test": yhat_test,
        "dates_train": dates[:split], "dates_test": dates[split:]
    }


# -----------------------------
# 4) One simple plot (timeline) + a 1-day-ahead forecast
# -----------------------------
def plot_timeline(res):                                   # draw one figure showing train/test actual vs predicted
    print("Plotting timeline...")
    plt.figure(figsize=(12, 5))                           # set the size so labels are readable
    plt.plot(res["dates_train"], res["y_train"], label="Actual (train)")      # train actual
    plt.plot(res["dates_train"], res["yhat_train"], label="Predicted (train)")# train predictions
    plt.plot(res["dates_test"],  res["y_test"],  label="Actual (test)")       # test actual
    plt.plot(res["dates_test"],  res["yhat_test"], label="Predicted (test)")  # test predictions
    if len(res["dates_test"]) > 0:                        # if there is a test set,
        plt.axvline(res["dates_test"][0], linestyle="--", label="Test start") # mark where it starts
    plt.title("ETH/USDT — Tomorrow's Close (simple model)")  # chart title
    plt.ylabel("Price (USDT)")                             # y-axis label
    plt.legend()                                           # show legend
    plt.tight_layout()                                     # tidy up spacing
    plt.show()                                             # render the plot


def forecast_tomorrow(model, X_full):                     # small helper to predict 1 day ahead
    """
    Quick 1-step-ahead forecast using the latest feature row.
    Multi-day forecasting is for later once I'm comfortable updating features step-by-step.
    """
    last_row = X_full.iloc[-1].values                     # take the last available feature row
    return float(model.predict([last_row])[0])            # run one prediction and return as a float


# -----------------------------
# 5) Main
# -----------------------------
def main():                                               # the script’s entry point
    print("=== Day 6: Simple ETH Price Predictor ===\n")  # header in console

    # Step 1: data
    df = fetch_eth_daily(days=365, symbol="ETHUSDT")      # download ~1 year of daily candles

    # Step 2: features
    X, y, dates = build_features(df)                      # build feature matrix X and target y

    # Step 3: train + evaluate
    res = train_and_evaluate(X, y, dates, train_ratio=0.8) # 80% train, 20% test (time-ordered)

    # Step 4: one clean plot
    plot_timeline(res)                                    # visualize model vs actual over time

    # Step 5: 1-day-ahead forecast from latest features
    X_full = pd.concat([X.loc[res["dates_train"]], X.loc[res["dates_test"]]]) # rebuild X in date order
    pred = forecast_tomorrow(res["model"], X_full)        # predict tomorrow’s close using the last row
    print(f"\nTomorrow's close forecast (ETH/USDT): {pred:.2f}")  # print the number

    # wrap up with a learning summary
    print("\nWhat I learned today:")
    print("- How to fetch real daily crypto data and turn it into a tidy DataFrame")
    print("- Why a time-ordered split matters for time series")
    print("- How to compare against a naïve baseline (keeps me honest)")
    print("- How to make a single, simple 1-day-ahead forecast")


if __name__ == "__main__":                                # only run main() if this file is executed directly
    main()                                                # call main()