stock = {
    "AAPL": {"price": 150.0, "shares": 100, "cost": 120.0},
    "GOOGL": {"price": 2800.0, "shares": 50, "cost": 2500.0},
    "AMZN": {"price": 3400.0, "shares": 20, "cost": 3000.0},
}

for ticker, data in stock.items():
    pnl = (data["price"] - data["cost"]) * data["shares"]
    print(f"{ticker}: P&L = ${pnl:.2f}")
    return_pct = (data["price"] - data["cost"]) / data["cost"] * 100
    print(f"{ticker}: Return = {return_pct:.2f}%")
    
total_pnl = sum((data["price"] - data["cost"]) * data["shares"] for data in stock.values())
print(f"Total P&L: ${total_pnl:.2f}")