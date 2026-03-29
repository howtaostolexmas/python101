import numpy as np
import matplotlib.pyplot as plt

all_prices = []  # เก็บทุก simulation

for sim in range(100):
    price = 100
    prices = [price]
    
    for day in range(252):
        daily_return = np.random.randn() * 0.02
        price = price * (1 + daily_return)
        prices.append(price)
    
    all_prices.append(prices)

all_prices = np.array(all_prices)  # shape: (100, 253)

# --- คำนวณ stats ---
avg_prices   = np.mean(all_prices, axis=0)
best_prices  = np.max(all_prices, axis=0)
worst_prices = np.min(all_prices, axis=0)
p10 = np.percentile(all_prices, 10, axis=0)  # แย่กว่า 90% ของกรณี
p90 = np.percentile(all_prices, 90, axis=0)  # ดีกว่า 90% ของกรณี

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 6))
days = range(253)

# เส้นทุก simulation (จางๆ)
for prices in all_prices:
    ax.plot(days, prices, alpha=0.1, color='gray', linewidth=0.8)

# Percentile band (P10-P90)
ax.fill_between(days, p10, p90, alpha=0.2, color='blue', label='P10–P90 Band')

# เส้นหลัก
ax.plot(days, worst_prices, color='red',    linewidth=2, label=f'Worst  (Day 252: {worst_prices[-1]:.1f})')
ax.plot(days, p10,          color='orange', linewidth=1.5, linestyle='--', label=f'P10    (Day 252: {p10[-1]:.1f})')
ax.plot(days, avg_prices,   color='blue',   linewidth=2, label=f'Avg    (Day 252: {avg_prices[-1]:.1f})')
ax.plot(days, p90,          color='green',  linewidth=1.5, linestyle='--', label=f'P90    (Day 252: {p90[-1]:.1f})')
ax.plot(days, best_prices,  color='darkgreen', linewidth=2, label=f'Best   (Day 252: {best_prices[-1]:.1f})')

# --- Summary box ---
final_prices = all_prices[:, -1]  # ราคาวันสุดท้ายของทุก sim
prob_profit = np.mean(final_prices > 100) * 100  # % ที่ได้กำไร

summary = (
    f"Final Day Summary\n"
    f"──────────────────\n"
    f"Best:   {best_prices[-1]:.2f}\n"
    f"P90:    {p90[-1]:.2f}\n"
    f"Avg:    {avg_prices[-1]:.2f}\n"
    f"P10:    {p10[-1]:.2f}\n"
    f"Worst:  {worst_prices[-1]:.2f}\n"
    f"──────────────────\n"
    f"P(profit): {prob_profit:.1f}%"
)
ax.text(0.02, 0.97, summary, transform=ax.transAxes,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

ax.set_title("Monte Carlo Simulation (100 paths)", fontsize=14)
ax.set_xlabel("Days")
ax.set_ylabel("Price")
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()