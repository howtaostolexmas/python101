import pandas as pd
import yfinance as yf   

df = yf.download("AAPL", start="2023-01-01", end="2024-01-01")
df["Return"] = df["Close"].pct_change() * 100

# Moving Average
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

# Cumulative Return
df["Cum_Return"] = (1 + df["Return"]/100).cumprod() - 1

print(df[["Close", "Return", "MA20", "MA50"]].tail(10))