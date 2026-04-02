import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("INTC", start="2025-01-01", end="2026-01-01")
df.columns = df.columns.droplevel(1)
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()
df["Return"] = df["Close"].pct_change() * 100
df["Cum_Return"] = (1 + df["Return"]/100).cumprod() - 1

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(df.index, df["Close"], color="blue", linewidth=2, label="Close Price")
axes[0, 0].plot(df.index, df["MA20"], color="orange", linewidth=2, label="MA20")
axes[0, 0].plot(df.index, df["MA50"], color="red", linewidth=2, label="MA50")
axes[0, 0].set_title("Price Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Price")
axes[0, 0].grid()
axes[0, 0].legend()

axes[0, 1].bar(df.index, df["Volume"], color="gray", alpha=0.7, label="Volume")
axes[0, 1].set_title("Trading Volume")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Volume")
axes[0, 1].grid()

axes[1, 0].hist(df["Return"].dropna(), bins=50, color="purple", alpha=0.7)
axes[1, 0].set_title("Return Distribution")
axes[1, 0].set_xlabel("Return (%)")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid()

axes[1, 1].plot(df.index, df["Cum_Return"], color="blue")
axes[1, 1].axhline(y=0, color="red", linestyle="--")
axes[1, 1].set_title("Cumulative Return")
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Return")
axes[1, 1].grid()

plt.tight_layout()
plt.show()
