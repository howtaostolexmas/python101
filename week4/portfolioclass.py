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

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def total_pnl(self):
        return sum(stock.pnl() for stock in self.stocks)

    def best_performer(self):
        return max(self.stocks, key=lambda stock: stock.return_pct())

    def summary(self):
        for stock in self.stocks:
            stock.summary()
        print(f"Total PnL: ${self.total_pnl():,.2f}")
        best = self.best_performer()
        print(f"Best Performer: {best.ticker} with a return of {best.return_pct():.2f}%")

port = Portfolio()
port.add_stock(Stock("NVDA", 200.0, 100, 150.0))
port.add_stock(Stock("TSMC", 120.0, 50, 100.0))
port.summary()