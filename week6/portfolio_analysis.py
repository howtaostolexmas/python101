import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download(["NVDA", "ASML", "TSM"], start="2025-01-01", end="2026-01-01")

returns_pct = df["Close"].pct_change() * 100
cum_returns = (1 + returns_pct / 100).cumprod() - 1
correlation = returns_pct.corr()

summary = (
    f"Correlation Matrix\n"
    f"──────────────────\n"
    f"NVDA-ASML: {correlation.loc['NVDA', 'ASML']:.2f}\n"
    f"NVDA-TSM:  {correlation.loc['NVDA', 'TSM']:.2f}\n"
    f"ASML-TSM:  {correlation.loc['ASML', 'TSM']:.2f}"
)
plt.text(0.02, 0.97, summary, transform=plt.gca().transAxes,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.plot(cum_returns["NVDA"], label="NVDA")
plt.plot(cum_returns["ASML"], label="ASML")
plt.plot(cum_returns["TSM"],  label="TSM")
plt.title("Cumulative Returns: NVDA vs ASML vs TSM (2025)")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()