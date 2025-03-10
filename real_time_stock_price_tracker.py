# -*- coding: utf-8 -*-
"""Real-Time Stock Price Tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ELcVzcIVel-uS9IKPYh9_CLFDS7ry7Om
"""

import requests

def get_stock_price(symbol, api_key):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "Global Quote" in data:
        price = data["Global Quote"]["05. price"]
        print(f"Current price of {symbol}: ${price}")
    else:
        print("Invalid stock symbol or API limit reached!")

if __name__ == "__main__":
    api_key = "your_api_key_here"  # Get your API key from https://www.alphavantage.co/
    symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ")
    get_stock_price(symbol, api_key)