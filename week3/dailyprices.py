def get_daily_prices():
    return list(map(float, input("ราคาหุ้นแต่ละวันในระยะเวลา 5 วัน: ").split()))
stock_prices = get_daily_prices()

while len(stock_prices) != 5:
    print("กรุณาใส่ราคาหุ้นจำนวน 5 วัน")
    stock_prices = get_daily_prices()

def daily_returns(stock_prices):
    returns = []
    for i in range(1, len(stock_prices)):
        daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1] * 100
        returns.append(daily_return)
    return returns

for i, daily_return in enumerate(daily_returns(stock_prices)):
    print(f"ผลตอบแทนรายวันวันที่ {i+2}: {daily_return:.2f}%")