buy_price = float(input("ราคาที่ซื้อ: "))
sell_price = float(input("ราคาที่ขาย: "))

print(f"ผลตอบแทน: {((sell_price - buy_price) / buy_price * 100):.2f}%")