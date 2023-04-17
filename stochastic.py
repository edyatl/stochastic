#!/usr/bin/env python3
"""
    Python porting of Stochastic TradingView Indicator
    Developed by @edyatl <edyatl@yandex.ru> April 2023
    https://github.com/edyatl

"""
# Standard imports
import pandas as pd
import numpy as np
import talib as tl
import os
from os import environ as env
from dotenv import load_dotenv
from binance import Client

# Load API keys from env
project_dotenv = os.path.join(os.path.abspath(""), ".env")
if os.path.exists(project_dotenv):
    load_dotenv(project_dotenv)

api_key, api_secret = env.get("ENV_API_KEY"), env.get("ENV_SECRET_KEY")

# Make API Client instance
client = Client(api_key, api_secret)

short_col_names = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "qav",
    "num_trades",
    "taker_base_vol",
    "taker_quote_vol",
    "ignore",
]

# Load Dataset
# Get last 500 records of BTCUSDT 15m Timeframe
klines = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_15MINUTE)
data = pd.DataFrame(klines, columns=short_col_names)

# Convert Open and Close time fields to DateTime
data["open_time"] = pd.to_datetime(data["open_time"], unit="ms")
data["close_time"] = pd.to_datetime(data["close_time"], unit="ms")

#--------------------------INPUTS--------------------------------
periodK: int = 14  # input.int(14, title="%K Length", minval=1)
smoothK: int = 3  # input.int(3, title="%K Smoothing", minval=1)
periodD: int = 3  # input.int(3, title="%D Smoothing", minval=1)

#--------------------------FUNCIONS------------------------------

def main():
    k, d = tl.STOCH(
        data["high"],
        data["low"],
        data["close"],
        periodK,
        smoothK,
        0,
        periodD,
        0,
    )
    res = pd.DataFrame(
        {
            "open_time": data["open_time"],
            "%K": k,
            "%D": d,
        }
    )
    res.to_csv('stochastic-BTCUSDT-15m.csv', index = None, header=True)


if __name__ == "__main__":
    main()
