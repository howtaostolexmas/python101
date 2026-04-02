import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("NVDA", start="2020-01-01")
df.columns = df.columns.get_level_values(0)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df["Close"])

max_idx = df["Close"].idxmax()
max_price = df["Close"].max()
min_idx = df["Close"].idxmin()
min_price = df["Close"].min()

ax.annotate(f"All time high: {max_price:.2f}", 
            xy=(max_idx, max_price), 
            xytext=(max_idx, max_price * 1.05), 
            arrowprops=dict(arrowstyle="->", color="green"),
            fontsize=10, color="green")
ax.annotate(f"All time low: {min_price:.2f}", 
            xy=(min_idx, min_price), 
            xytext=(min_idx, min_price * -5),
            arrowprops=dict(arrowstyle="->", color="red"),
            fontsize=10, color="red")
ax.set_title("NVDA Closing Price with Annotations")
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price (USD)")
plt.grid()
plt.show()