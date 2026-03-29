import numpy as np

prices = np.array([100, 105, 98, 110, 95, 120, 115, 130, 125, 140])

daily_returns = np.diff(prices) / prices[:-1] * 100
print(f"Daily Returns: {daily_returns}%")

mean_return = np.mean(daily_returns)
print(f"Mean Return: {mean_return:.2f}%")

std_deviation = np.std(daily_returns, ddof=1)
print(f"Standard Deviation of Returns: {std_deviation:.2f}%")

positive_returns = daily_returns[daily_returns > 0]
print(f"Positive Daily Returns: {positive_returns}%")