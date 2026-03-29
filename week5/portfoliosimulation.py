import numpy as np

prices = np.array([
    [100, 105, 98, 110, 95, 120, 115, 130, 125, 140],  # AAPL
    [200, 195, 210, 205, 215, 220, 218, 225, 230, 235], # TSLA
    [80, 85, 82, 88, 90, 87, 92, 95, 91, 98]            # AMD
])

tickers = ["AAPL", "TSLA", "AMD"]

daily_returns = np.diff(prices, axis=1) / prices[:, :-1] * 100
mean_returns = np.mean(daily_returns, axis=1)
best_idx = np.argmax(mean_returns)

print(f"Daily Returns:{daily_returns}%")
print(f"Mean Returns:{mean_returns}%")
print(f"Best Performing Asset: {tickers[best_idx]} {mean_returns[best_idx]:.2f}%")