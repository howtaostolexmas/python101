import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns   

tickers = [
    # Tech
    "NVDA", "AAPL", "MSFT", "GOOGL",
    # Semiconductor  
    "ASML", "TSM", "AMD", "INTC",
    # Finance
    "JPM", "GS", "BAC",
    # Energy
    "XOM", "CVX",
    # Healthcare
    "JNJ", "PFE",
    # Consumer
    "AMZN", "TSLA", "WMT",
    # ETF
    "SPY", "QQQ"
]

df = yf.download(tickers, start="2025-01-01", end="2026-01-01")
returns_pct = df["Close"].pct_change() * 100
correlation = returns_pct.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation, annot=True,fmt=".2f", cmap="coolwarm")

plt.title("Correlation Heatmap of Stock Returns (2025)")
plt.tight_layout()
plt.show()