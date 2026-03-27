stock_prices = list(map(float, input("ราคาหุ้นแต่ละตัว: ").split()))

print(f"ราคาหุ้นสูงสุด: {max(stock_prices):.2f} บาท")
print(f"ราคาหุ้นต่ำสุด: {min(stock_prices):.2f} บาท")
print(f"ราคาหุ้นเฉลี่ย: {sum(stock_prices) / len(stock_prices):.2f} บาท")

for i, price in enumerate(stock_prices):
    if price > 100:
        print(f"ราคาหุ้นตัวที่ {i+1}: {price:.2f} บาท สูงกว่า 100 บาท")