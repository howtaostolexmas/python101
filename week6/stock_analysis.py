import yfinance as yf   
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2025-01-01", end="2026-01-01")

df["Return"] = df["Close"].pct_change() * 100
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()
df["Cum_Return"] = (1 + df["Return"]/100).cumprod() - 1
best_day  = df["Return"].idxmax()
worst_day = df["Return"].idxmin()


print(df[["Close", "Return", "MA20", "MA50"]].tail(10))
print(f"Best Return Day: {best_day}")
print(f"Return: {df['Return'][best_day]:.2f}%")
print(f"Worst Return Day: {worst_day}")
print(f"Return: {df['Return'][worst_day]:.2f}%")

plt.figure(figsize=(14, 7))
plt.plot(df.index, df["Close"], label=f"Close Price")
plt.plot(df.index, df["MA20"], label=f"MA20")
plt.plot(df.index, df["MA50"], label=f"MA50")
plt.title("AAPL Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()