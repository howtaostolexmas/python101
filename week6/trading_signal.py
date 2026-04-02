import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AMZN", start="2025-01-01", end="2026-01-01")

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

golden_cross = (df["MA20"] > df["MA50"]) & (df["MA20"].shift(1) < df["MA50"].shift(1))
death_cross  = (df["MA20"] < df["MA50"]) & (df["MA20"].shift(1) > df["MA50"].shift(1))

plt.figure(figsize=(14, 7))
plt.plot(df.index, df["Close"], label="Close Price")
plt.plot(df.index, df["MA20"], label="MA20")
plt.plot(df.index, df["MA50"], label="MA50")
plt.scatter(df.index[golden_cross], df["Close"][golden_cross], marker="^", color="green", s=100, label="Buy")
plt.scatter(df.index[death_cross], df["Close"][death_cross], marker="v", color="red", s=100, label="Sell")

plt.title("AMZN MA20/MA50 Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()