class Stock:
    def __init__(self, ticker, price, shares, cost):
        self.ticker = ticker
        self.price  = price
        self.shares = shares
        self.cost   = cost

    def pnl(self):
        return (self.price - self.cost) * self.shares

    def return_pct(self):
        return (self.price - self.cost) / self.cost * 100
    
    def update_price(self, new_price):
        self.price = new_price

    def summary(self):
        return print(f"{self.ticker}: Price={self.price:,.2f}, Shares={self.shares:,.2f}, Cost={self.cost:,.2f}")

stock = [
    Stock("NVDA", 200.0, 100, 150.0),
    Stock("TSMC", 120.0, 50, 100.0),
    Stock("AMD", 80.0, 20, 60.0)
    ]

new_prices = {
    "NVDA": 250.0,
    "TSMC": 135.0,
    "AMD" : 75.0
}

for s in stock:
    if s.ticker in new_prices:
        s.update_price(new_prices[s.ticker])
    s.summary()
    print(f"{s.ticker}: P&L = ${s.pnl():.2f}")
    print(f"{s.ticker}: Return = {s.return_pct():.2f}%")
