tickers = set()
trades = []

with open('trades.txt', 'r') as f:
    for line in f:
        ticker, price, counts = line.strip().split(',')
        price = float(price)
        counts = int(counts)
        total_price = price * counts
        tickers.add(ticker)
        trades.append((ticker, price, counts, total_price))

for trade in trades:
    print(f"ชื่อ ticker: {trade[0]}, ราคา: {trade[1]:.2f}, มูลค่า: {trade[3]:,.2f}")
print(f"\nUnique tickers ({len(tickers)}): {', '.join(tickers)}")